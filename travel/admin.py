from django.contrib import admin

from travel.models import Travel


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    pass
