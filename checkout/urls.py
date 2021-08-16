from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('thank-you/', views.thank_you, name='thank-you'),
    path('stripe_webhook/', views.stripe_webhook, name="stripe_webhook")

]
