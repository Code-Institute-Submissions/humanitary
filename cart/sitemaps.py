from django .contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class CartViewSitemap(Sitemap):
    def items(self):
        return ['cart']

    def location(self, item):
        return reverse(item)
