import stripe
import json
from accounts.models import *
from shop.models import *
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
import os
STRIPE_PRIVATE_KEY = os.environ.get('STRIPE_PRIVATE_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
stripe.api_key = STRIPE_PRIVATE_KEY

# This file is where I've put the logic for my checkout page, my cart data and the checkout session. I put it here in order to clean up my views


def cookieCart(request):
    """ Returns a cookie that represents the guest users cart """

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
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    """ Gets the data from the cart and returns it as a dictionary """

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        items = cookieData['items']
        cartItems = cookieData['cartItems']
    return {'cartItems': cartItems, 'order': order, 'items': items}


def getItems(request, my_list):
    """ Gets the items from the cart and adds them to the stripe
    checkout session """

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
    return cart_items


def updateCart(request):
    """ Adds and removes quantities of items to/from the shopping cart """

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    elif action == 'delete':
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def checkout_session(request):
    """ Takes in getItems and cartData and uses that information to display
    the current products and amount to pay in the stripe checkout session """

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=getItems(request, cartData(request)['items']),

        # Used code snippet from Denis Ivy's tutorial on
        # django E-commerce, although somewhat modified to fit my own needs.

        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('cart')),
    )

    context = {
        'session_id': session.id,
        'session': session,
        'stripe_public_key': STRIPE_PUBLIC_KEY,
    }
    return context
