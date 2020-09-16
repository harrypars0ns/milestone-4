from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'readable_name',

    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nation_of_origin',
        'price',
        'image',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
