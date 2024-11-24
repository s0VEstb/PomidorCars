from django.contrib import admin
from . import models


admin.site.register(models.ABitInfoAboutUs)


class SlogansNumbersInline(admin.TabularInline):  # Или admin.StackedInline
    model = models.SlogansNumbers
    extra = 1  # Количество пустых строк для добавления новых записей
    fields = ['number', 'text']  # Поля, которые будут отображаться

# Inline для модели SlogansText
class SlogansTextInline(admin.TabularInline):  # Или admin.StackedInline
    model = models.SlogansText
    extra = 1  # Количество пустых строк для добавления новых записей
    fields = ['title', 'description']

# Админка для модели OurSlogan
@admin.register(models.OurSlogan)
class OurSloganAdmin(admin.ModelAdmin):
    inlines = [SlogansNumbersInline, SlogansTextInline]
    list_display = ['__str__']  # Отображаемое имя в списке


class ProudRewards(admin.TabularInline):
    model = models.ProudRewards
    extra = 1
    fields = ['image', 'description']


@admin.register(models.OurProud)
class OurProudAdmin(admin.ModelAdmin):
    inlines = [ProudRewards]
    list_display = ['__str__']


class CompanyAuthors(admin.TabularInline):
    model = models.CompanyAuthors
    extra = 1
    fields = ['name', 'url_1', 'url_2']


@admin.register(models.CompanyAuthorsInfo)
class CompanyAuthorsInfoAdmin(admin.ModelAdmin):
    inlines = [CompanyAuthors]
    list_display = ['__str__']


