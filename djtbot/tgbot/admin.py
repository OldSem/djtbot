from django.contrib import admin
from .models import *


@admin.register(CategoryClothe)
class CategoryClothesAdmin(admin.ModelAdmin):
    pass


@admin.register(Male)
class MaleAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ('name',)
    search_fields = ['user']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_filter = ('name',)
    search_fields = ['user']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created')
    date_hierarchy = 'created'
    list_filter = ('first_name',)
    search_fields = ['first_name']


@admin.register(Clothe)
class ClothesAdmin(admin.ModelAdmin):
    fields = (('partner', 'male', 'currency'),
              ('category', 'country'),
              ('img_center', 'img_inline', 'img_bottom'),
              ('description', 'article_id', 'price', 'markup', 'is_active'))

    list_display = ('article_id', 'img_center', 'partner', 'markup', 'is_active', 'male', 'country')
    list_filter = ('article_id', 'is_active', 'partner')
    search_fields = ['article_id']


@admin.register(CategoryPrice)
class CategoryPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass


@admin.register(ClotheMale)
class ClothesMaleAdmin(admin.ModelAdmin):
    pass


@admin.register(ClotheCountry)
class ClothesCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(ClothePartner)
class ClothesPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    list_filter = ('name',)
    search_fields = ['name']


@admin.register(SystemPhoto)
class SystemFotoAdmin(admin.ModelAdmin):
    pass


@admin.register(HistoryUpdateId)
class HistoryUpdateIdAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'article', 'created', 'price', 'markup')
    date_hierarchy = 'created'
    list_filter = ('first_name', 'sent', 'have_ordered', 'paid')
    search_fields = ['first_name']
