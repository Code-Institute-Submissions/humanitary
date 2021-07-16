from django.shortcuts import render
from .models import Products
# Create your views here.


def shop(request):

    products = Products.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'shop/products.html', context)
