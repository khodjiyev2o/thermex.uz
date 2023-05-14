from django.contrib import admin
from .models import Category, Product, SoldProduct, Brand
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'point')
    list_display_links = ('id', 'name')
    search_fields = (
        'id',
        'name'
        'brand__name',
        'point',
    )


@admin.register(SoldProduct)
class SoldProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'user', 'product', 'barcode', 'created_at')
    search_fields = (
        'user__phone',
        'product__name',
        'barcode',
        'created_at',
        'city___name',
    )
