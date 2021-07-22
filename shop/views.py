from django.shortcuts import render
from .models import Product
from accounts.models import *

# Snippets taken from code institutes lesson on django ecommerce.


def shop(request):
    products = Product.objects.all()
    context = {'products': products, }
    return render(request, 'shop/products.html', context)
