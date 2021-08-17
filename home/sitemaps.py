from django .contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class HomeViewSitemap(Sitemap):
    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
