from django.contrib import admin
from .models import Category, Product

class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CatergoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_quantity', 'created_date', 'available']
    list_filter = ['created_date','category', 'available']
    list_editable = ['price', 'stock_quantity', 'available']
    search_fields = ['name', 'category', 'available']

admin.site.register(Product, ProductAdmin)

