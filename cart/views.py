from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """ A view to return and view the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Select a quantity of an item and add it to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """ Select a quantity of an item and edit it in the cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """ Delete an item from the cart by setting it's quantity to 0 """

    cart = request.session.get('cart', {})
    del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
