from cart.contexts import cartItems
from django.http.response import HttpResponse
from django.shortcuts import render
from humanitary_gift_shop.utils import checkout_session
from django.views.decorators.csrf import csrf_exempt
import stripe
import os
STRIPE_PRIVATE_KEY = os.environ.get('STRIPE_PRIVATE_KEY')
stripe.api_key = STRIPE_PRIVATE_KEY

# Create your views here.


# For more on the 'checkout_session' function, refer to the utils.py in the root folder


def checkout(request):
    """ This view renders the checkout and stripe page """

    return render(request, 'checkout/checkout.html', checkout_session(request))


@csrf_exempt
def stripe_webhook(request):
    print('webhook!')

    endpoint_secret = 'whsec_hKGJ5sOTNMBs8eJkulxzxIrDuxOL9Mj4'
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
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        cartItems = {}
        print(session, cartItems)

    # Passed signature verification
    return HttpResponse(status=200)
