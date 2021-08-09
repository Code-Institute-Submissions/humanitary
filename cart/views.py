from django.shortcuts import render
from accounts.models import *
from shop.models import *
from django.http import JsonResponse
import json

# Create your views here.

# Used code from Dennis Ivy's tutorial on
# django E-commerce, although modified to fit my own needs.


def shopping_cart(request):
    """ Renders the shopping cart page and cart content """

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'cart/cart.html', context)


def updateCart(request):
    """ Adds and removes quantities of items to/from the shopping cart """

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    if request.user.is_authenticated:
        customer = request.user.customer
    else:
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

    return JsonResponse('Item was added', safe=False)
