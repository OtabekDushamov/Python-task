from django.contrib import admin
from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent',)
    search_fields = ('title',)
    autocomplete_fields = ('parent',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'shop', 'category', 'amount', 'price', 'active')
    list_editable = ('amount', 'price', 'active')
    list_filter = ('shop', 'category')
    search_fields = ('id', 'title')
    autocomplete_fields = ('shop', 'category')
    readonly_fields = ('images',)


@admin.register(Product_image)
class Product_imageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_filter = ('product__title',)
    autocomplete_fields = ('product',)
