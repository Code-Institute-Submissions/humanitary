from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name="cart"),
    path('update_cart/', views.updateCart, name="update_cart")

]
