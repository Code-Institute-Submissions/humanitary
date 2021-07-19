from django.shortcuts import render

# Create your views here.


def shopping_cart(request):
    """ Renders the shopping cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Adds the specified item to the shopping cart """
