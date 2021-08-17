from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from accounts.models import Order


@xframe_options_exempt
def index(request):
    """ Renders the home page """

    return render(request, 'home/index.html')
