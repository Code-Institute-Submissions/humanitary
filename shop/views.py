from django.shortcuts import render
from .models import Product
# Create your views here.


def shop(request):

    product = Product.objects.all()

    context = {
        'products': product,
    }
    return render(request, 'shop/products.html', context)
