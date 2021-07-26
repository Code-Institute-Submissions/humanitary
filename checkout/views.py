from django.shortcuts import render
from django.urls import reverse
from accounts.models import *
from humanitary_gift_shop.secretstuff import STRIPE_PRIVATE_KEY, STRIPE_PUBLIC_KEY
import stripe

stripe.api_key = STRIPE_PRIVATE_KEY

# Create your views here.

# Used code snippets from Denis Ivy's tutorial on
# django E-commerce, although somewhat modified to fit my own needs.


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
        }

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                # TODO: replace this with the `price` of the product you want to sell
                'price': 'price_1JGnQtB2DZm9V6pJJaJavDS1',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('cart')),
    )

    context = {
        'items': items,
        'order': order,
        'session_id': checkout_session.id,
        'checkout_session': checkout_session,
        'stripe_public_key': STRIPE_PUBLIC_KEY,
    }

    return render(request, 'checkout/checkout.html', context)
