from allauth.account.forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer
from django.contrib.auth.models import Group, User


# Create your views here.

@login_required
def profile_page(request):
    return render(request, 'accounts/profile.html')
