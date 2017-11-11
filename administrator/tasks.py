import xlrd

from inventory.models import Category, Merchandise, Transaction


def import_transaction(transaction_data, filename):
    try:
        book = xlrd.open_workbook(filename=filename)
        sheet = book.sheet_by_index(0)
    except FileNotFoundError:
        raise Exception('No such file: {}'.format(filename))

    header = sheet.row_values(3, 0)
    dataset = [dict(zip(header, sheet.row_values(rx))) for rx in range(4, sheet.nrows)]

    category = None
    for data in dataset:
        try:
            int(data['No.'])
            if data['대분류'] != '':
                category, created = Category.objects.get_or_create(name=data['대분류'])
            price = int(data['총매출액']) / int(data['수량'])
            merchandise, created = Merchandise.objects.get_or_create(code=data['상품코드'],
                                                                     defaults={
                                                                         'name': data['상품명'],
                                                                         'category': category,
                                                                         'price': price,
                                                                     })

            Transaction.objects.create(merchandise=merchandise,
                                       type='SELL',
                                       quantity=int(data['수량']),
                                       date=transaction_data.date,
                                       transaction_data=transaction_data)
        except ValueError:
            pass
