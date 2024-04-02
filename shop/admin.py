from django.contrib import admin
from django.utils.html import format_html
from .models import *
from .filters import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent',)
    search_fields = ('title', 'parent__title')
    autocomplete_fields = ('parent',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('first_image', 'title', 'shop', 'category', 'amount', 'price', 'active')
    list_editable = ('amount', 'price', 'active')
    list_filter = ('shop', 'category', 'active', PriceRangeFilter)
    search_fields = ('id', 'title')
    autocomplete_fields = ('shop', 'category')
    readonly_fields = ('images', 'first_image')

    def first_image(self, obj):
        first_image = Product_image.objects.filter(product=obj).first()
        if first_image:
            return format_html('<div style="width: 45px; height: 28px;"><img src="{}" style="width: 100%; height: 100%; object-fit: cover;" /><div>', first_image.image.url)
        return 'No Image'

    first_image.short_description = 'Фотография'


@admin.register(Product_image)
class Product_imageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_filter = ('product__title',)
    autocomplete_fields = ('product',)
