from django.contrib import admin
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


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ['code', 'category', 'name', 'formatted_price']
    list_filter = ['category']

    class Media:
        css = {
            'all': ('admin/css/admin.css',)
        }

    @short_description('price')
    def formatted_price(self, obj):
        return '{:,} 원'.format(obj.price)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchandise', 'type', 'quantity', 'date', 'create_user']
    list_filter = ('merchandise', 'type', ('date', DateRangeFilter))
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
