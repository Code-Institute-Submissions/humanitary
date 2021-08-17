from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path("robots.txt", views.robots_txt),

]
