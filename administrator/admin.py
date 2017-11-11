from django.contrib import admin

from administrator.models import TransactionData


@admin.register(TransactionData)
class TransactionDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'file', 'created_at']
