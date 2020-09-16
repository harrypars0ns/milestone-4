from django import forms
from .models import Category, Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'category', 'description',
                  'nation_of_origin', 'price', 'image_url',)
        model = Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product_categories = Category.objects.all()
        readable_names = [(category.id, category.get_readable_name())
                          for category in product_categories]

        self.fields['category'].choices = readable_names
