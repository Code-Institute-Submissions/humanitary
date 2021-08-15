from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField
from shop.models import Product

# Create your models here.

# Used these models from Dennis Ivy's Tutorial on
# django E-commerce.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = CharField(max_length=200, null=True)
    email = CharField(max_length=200, null=True)
    device = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_quantity_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __def__(self):
        return self.product.name
