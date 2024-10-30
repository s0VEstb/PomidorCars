from django.contrib import admin
from .models import CarModel, MarkModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']
    list_filter = ['price']


admin.site.register(MarkModel)