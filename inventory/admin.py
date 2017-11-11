from django.contrib import admin
from jet.filters import DateRangeFilter

from inventory.models import Merchandise, Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchandise', 'type', 'quantity', 'date']
    list_filter = ('merchandise', 'type', ('date', DateRangeFilter))
