from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import *
from shop.models import *


# Create your views here.

@login_required
def profile_page(request):
    completed_orders_list = []

    customer = request.user.customer
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    completed_orders = Order.objects.filter(
        customer=customer, complete=True)
    completed_orders_list = []

    for item in completed_orders:
        completed_orders_list.append(item)

    all_order_items = OrderItem.objects.all()

    context = {
        'customer_name': customer,
        'customer_email': customer.email, 'items': items, 'order': order,
        'cartItems': cartItems, 'completed_orders': completed_orders, "all_order_items": all_order_items, "completed_orders_list": completed_orders_list}

    return render(request, 'accounts/profile.html', context)
