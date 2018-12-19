from django.contrib import admin
from .models import *


@admin.register(CategoryClothes)
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
    pass


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'img_top', 'is_active', 'male', 'country')
    list_display_links = ('article_id', 'male', 'country')
    list_filter = ('article_id', 'is_active')
    search_fields = ['article_id']

    class Media:
        css = {'all': ('css/admin/myadmin.css',)}


@admin.register(CategoryPrice)
class CategoryPriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass


@admin.register(ClothesMale)
class ClothesMaleAdmin(admin.ModelAdmin):
    pass


@admin.register(ClothesCountry)
class ClothesCountryAdmin(admin.ModelAdmin):
    pass
