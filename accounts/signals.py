from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import Customer


@receiver(user_signed_up)
def new_customer(sender, **kwargs):
    p = Customer(
        user=kwargs['user'],
        name=kwargs['user'],
    )
    p.save()
