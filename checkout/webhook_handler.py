from django.http import HttpResponse

from .models import Order, OrderLineItem
from profiles.models import UserProfile
from products.models import Product

import time
import json


class StripeWH_Handler:
    """Handles stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles an unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhooks
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        # billing_details = intent.charges.data[0].billing_details
        shipping = intent.charges.data[0].shipping
        cart_plus_ship = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping.address.items():
            if value == '':
                shipping.address[field] = None

        # update info checkbox

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping.phone
                profile.default_country = shipping.address.country
                profile.default_postcode = shipping.address.postal_code
                profile.default_town_or_city = shipping.address.city
                profile.default_street_address1 = shipping.address.line1
                profile.default_street_address2 = shipping.address.line2
                profile.default_county = shipping.address.state
                profile.save()


        order_exists = False
        order_attempt = 1
        while order_attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping.name,
                    phone_number__iexact=shipping.phone,
                    country__iexact=shipping.address.country,
                    postcode__iexact=shipping.address.postal_code,
                    town_or_city__iexact=shipping.address.city,
                    street_address1__iexact=shipping.address.line1,
                    street_address2__iexact=shipping.address.line2,
                    county__iexact=shipping.address.state,
                    cart_plus_ship=cart_plus_ship,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                order_attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} |\
                     SUCCESS: Order in database already',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping.name,
                    user_profile=profile,
                    phone_number=shipping.phone,
                    country=shipping.address.country,
                    postcode=shipping.address.postal_code,
                    town_or_city=shipping.address.city,
                    street_address1=shipping.address.line1,
                    street_address2=shipping.address.line2,
                    county=shipping.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in \
                             item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment_intent.payment_failed webhooks
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
