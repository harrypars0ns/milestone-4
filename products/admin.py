from django.contrib import admin
from .models import Category, Product, Continent, SustainableTrait


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',

    )


class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'name',

    )


class SustainableTraitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nation_of_origin',
        'price',
        'image',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(SustainableTrait, SustainableTraitAdmin)
admin.site.register(Product, ProductAdmin)
