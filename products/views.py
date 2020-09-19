from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ProductAdminForm
from .models import Product


def create_product(request):
    """A view to create a product"""
    if request.method == 'POST':
        product_admin_form = ProductAdminForm(request.POST, request.FILES)
        if product_admin_form.is_valid:
            the_product = product_admin_form.save()
            return redirect(reverse('get_product', args=[the_product.id]))
    else:
        product_admin_form = ProductAdminForm()

    template = 'products/create_product.html'
    context = {
        'product_admin_form': product_admin_form,
    }
    return render(request, template, context)


def edit_product(request, product_id):
    """A view to Edit a product"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_admin_form = ProductAdminForm(request.POST,
                                              request.FILES, instance=product)
        if product_admin_form.is_valid:
            product_admin_form.save()
            return redirect(reverse('get_product', args=[product.id]))
    else:
        product_admin_form = ProductAdminForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'product_admin_form': product_admin_form,
        'product': product,
    }
    return render(request, template, context)


def remove_product(request, product_id):
    """A view to delete a product"""
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))


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
