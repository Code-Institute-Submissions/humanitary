from django.shortcuts import render
from accounts.models import *

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
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout/checkout.html', context)
