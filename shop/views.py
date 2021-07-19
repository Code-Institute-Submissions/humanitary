from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Product


def shop(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'shop/products.html', context)


def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)
    return JsonResponse('Item was added', safe=False)
