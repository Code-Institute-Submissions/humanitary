from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver
from .models import Customer, Order


@receiver(user_signed_up)
def new_customer(sender, **kwargs):
    p = Customer(
        user=kwargs['user'],
        name=kwargs['user'],
    )
    p.save()
