from django.shortcuts import render
from humanitary_gift_shop.utils import checkout_session


# Create your views here.


""" For more on the 'checkout_session' function, refer to the utils.py in the root folder """


def checkout(request):
    """ This view renders the checkout and stripe page """

    return render(request, 'checkout/checkout.html', checkout_session(request))
