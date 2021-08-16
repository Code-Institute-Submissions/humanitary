from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse, HttpRequest


@xframe_options_exempt
def index(request):
    """ Renders the home page """

    return render(request, 'home/index.html')
