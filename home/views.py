from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request):
    """ Renders the home page """

    return render(request, 'home/index.html')


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
