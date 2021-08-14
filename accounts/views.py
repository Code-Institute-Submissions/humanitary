from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def profile_page(request):
    customer = request.user.customer
    email = request.user.email

    context = {
        'customer_name': customer,
        'customer_email': email,
    }

    return render(request, 'accounts/profile.html', context)
