from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.conf import settings


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


@xframe_options_exempt
def index(request):
    """ Renders the home page """

    return render(request, 'home/index.html')


def subscribe(request):
    """ Renders the page after newsletter sub """

    return render(request, 'home/subscribe.html')


def error_404(request, exception):
    data = {}
    return render(request, 'home/404.html', data)


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /checkout/thank-you.html/",
        "Disallow: /accounts/login.html/",
        "Disallow: /accounts/logout.html/"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
