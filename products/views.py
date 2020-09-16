from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductAdminForm


def create_product(request):
    product_admin_form = ProductAdminForm()
    template = 'products/create_product.html'
    context = {
        'product_admin_form': product_admin_form,
    }
    return render(request, template, context)


def all_products(request):
    """ All products view """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def get_product(request, product_id):
    """ Get an individual product's view """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/get_product.html', context)

