from django.contrib import admin
from .models import CarModel, MarkModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'mark']
    search_fields = ['name', 'mark__name']
    list_filter = ['price', 'mark']


admin.site.register(MarkModel)