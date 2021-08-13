from django.shortcuts import render
from django.urls import reverse
from accounts.models import *
from shop.models import *
from humanitary_gift_shop.secretstuff import STRIPE_PRIVATE_KEY, STRIPE_PUBLIC_KEY
import stripe
import json

stripe.api_key = STRIPE_PRIVATE_KEY

# Create your views here.


def checkout(request):
    """ This view creates a checkout session in stripe on the checkout page,
    and fetches the information from the API needed to pay the correct amount """

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

        for i in cart:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'image': product.image,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total
            }
            items.append(item)

    def getItems(my_list):
        """ Gets the items from the cart and adds them to the stripe
        checkout sessions """

        cart_items = []
        if request.user.is_authenticated:
            for item in my_list:
                intitial_price = item.product.price * 100
                converted_price = int(intitial_price)

                products = {
                    'name': item.product.name,
                    'quantity': item.quantity,
                    'amount': converted_price,
                    'currency': 'usd'
                }
                cart_items.append(products)
            print(cart_items)
            return cart_items

        for item in my_list:
            intitial_price = item['product']['price'] * 100
            converted_price = int(intitial_price)

            products = {
                'name': item['product']['name'],
                'quantity': item['quantity'],
                'amount': converted_price,
                'currency': 'usd'
            }
            cart_items.append(products)
            print(cart_items)
            return cart_items

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=getItems(items),
        # Used code snippet from Denis Ivy's tutorial on
        # django E-commerce, although somewhat modified to fit my own needs.
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('cart')),
    )

    context = {
        'session_id': checkout_session.id,
        'checkout_session': checkout_session,
        'stripe_public_key': STRIPE_PUBLIC_KEY,
    }
    return render(request, 'checkout/checkout.html', context)
