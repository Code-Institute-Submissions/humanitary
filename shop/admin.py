from django.contrib import admin
from .models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'image',
    )


admin.site.register(Products, ProductAdmin)
