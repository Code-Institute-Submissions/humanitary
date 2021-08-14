from accounts.models import *
from shop.models import *
from humanitary_gift_shop.utils import cookieCart


def cartItems(request):
    """ Checks if the user is authenticated, and if it is,
    it checks for the orders in the database and renders them on
    the page. Otherwise, it creates a cookie object that represents the cart
    and renders that instead """

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

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return context
