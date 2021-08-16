import urllib.request
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from accounts.models import Order, Customer
from humanitary_gift_shop.utils import checkout_session, random_string_generator, cookieCart
from django.views.decorators.csrf import csrf_exempt
import stripe
import os

STRIPE_PRIVATE_KEY = os.environ.get('STRIPE_PRIVATE_KEY')
stripe.api_key = STRIPE_PRIVATE_KEY

# Create your views here.


# For more on the 'checkout_session' function, refer to the utils.py in the root folder


def checkout(request):
    """ This view renders the checkout and stripe page """
    try:
        customer = request.user.customer
        order = Order.objects.get(
            customer=customer, complete=False)
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    return render(request, 'checkout/checkout.html', checkout_session(request))


def thank_you(request):
    return render(request, 'checkout/thank-you.html')


@ csrf_exempt
def stripe_webhook(request):

    endpoint_secret = os.environ.get('endpoint_secret')
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event

    # Saves the order as complete
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer = session['metadata']['customer']

        order = Order.objects.get(
            customer=customer, complete=False)
        order.complete = True
        order.transaction_id = random_string_generator()
        order.save()
    # Passed signature verification
    return HttpResponse(status=200)
