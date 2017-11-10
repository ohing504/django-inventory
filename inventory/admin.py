from django.contrib import admin

from inventory.models import Merchandise, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    pass
