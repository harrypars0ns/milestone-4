from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ProductAdminForm
from .models import Product, Category


def create_product(request):
    if request.method == 'POST':
        product_admin_form = ProductAdminForm(request.POST, request.FILES)
        if product_admin_form.is_valid:
            product_admin_form.save()
            return redirect(reverse('create_product'))
    else:
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

