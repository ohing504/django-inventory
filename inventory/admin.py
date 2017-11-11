from django.contrib import admin, messages
from jet.filters import DateRangeFilter

from inventory.models import Merchandise, Category, Transaction

admin.site.disable_action('delete_selected')


def short_description(desc=None):
    def decorate(func):
        if desc:
            func.short_description = desc
        return func
    return decorate


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class MerchandiseAdminAction(admin.ModelAdmin):

    @short_description('선택한 상품의 수량 초기화')
    def init_quantity(self, request, queryset):
        if request.user.is_superuser:
            queryset.update(quantity=0)
            self.message_user(request, 'Successfully initialize quantity as 0.', level=messages.SUCCESS)
        else:
            self.message_user(request, "You don't have permission.", level=messages.ERROR)

    actions = [init_quantity]


@admin.register(Merchandise)
class MerchandiseAdmin(MerchandiseAdminAction):
    list_display = ['code', 'category', 'name', 'quantity', 'formatted_price']
    list_filter = ['category']
    readonly_fields = ['quantity']

    class Media:
        css = {
            'all': ('admin/css/admin.css',)
        }

    @short_description('price')
    def formatted_price(self, obj):
        return '{:,} 원'.format(obj.price)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['merchandise', 'quantity', 'date', 'create_user', 'note']
    list_filter = ('merchandise', ('date', DateRangeFilter))
    fields = ['merchandise', 'quantity', 'date', 'note', 'transaction_data', 'create_user']
    readonly_fields = ['create_user']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

    @staticmethod
    @short_description('created By')
    def create_user(obj):
        user = obj.created_by
        if user is not None:
            if user.first_name is not '':
                return '{}{}'.format(user.last_name, user.first_name)
            else:
                return user.username
        else:
            return '-'
