from django .contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class CheckoutViewSitemap(Sitemap):
    def items(self):
        return ['checkout']

    def location(self, item):
        return reverse(item)
