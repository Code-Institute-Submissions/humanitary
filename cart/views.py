from django.shortcuts import render
from accounts.models import *
from shop.models import *
from humanitary_gift_shop.utils import updateCart


# Used code from Dennis Ivy's tutorial on
# django E-commerce, although modified to fit my own needs.

def shopping_cart(request):
    """ Renders the shopping cart page and cart content """
    try:
        customer = request.user.customer

    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    return render(request, 'cart/cart.html')
