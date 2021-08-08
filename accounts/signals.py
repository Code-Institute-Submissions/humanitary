from allauth.account.signals import user_signed_up
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Customer


@receiver(user_signed_up)
def new_customer(sender, **kwargs):
    p = Customer(
        user=kwargs['user'],
        name=kwargs['user'],
    )
    p.save()
