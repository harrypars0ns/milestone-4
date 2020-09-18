from django.contrib import admin
from .models import Order, OrderLineItem

# Admin


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

# Fields for admin to display for each order


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'order_total', 'cart_plus_ship',
                       'original_cart', 'stripe_pid',)

    fields = ('order_number', 'date', 'full_name',
              'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2',
              'order_total', 'cart_plus_ship', 'original_cart', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'cart_plus_ship',)

    ordering = ('-date',)

# Registration


admin.site.register(Order, OrderAdmin)
