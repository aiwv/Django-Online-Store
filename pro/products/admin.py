from django.contrib import admin

# Register your models here.
from .models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ('name', 'desc', ('price', 'quantity'), 'image', 'category',)
    # readonly_fields = ('desc',)
    search_fields = ('name',)
    ordering = ('name',)