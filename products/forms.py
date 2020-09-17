from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description', 'category', 'continent',
                  'sustainable_trait', 'nation_of_origin', 'price', 'image',)
        model = Product
