from django .contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class ShopViewSitemap(Sitemap):
    def items(self):
        return ['shop']

    def location(self, item):
        return reverse(item)
