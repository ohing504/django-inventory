from django.contrib import admin

from administrator.models import TransactionData
from inventory.admin import short_description


@admin.register(TransactionData)
class TransactionDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'file_name', 'created_at']

    @staticmethod
    @short_description('file')
    def file_name(obj):
        return obj.file.name
