# from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Product(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    avg_cost = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

# class Supplier(models.Model):
#     code = models.CharField(max_length=10)
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     email = models.EmailField()
#     created_dt = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     updated_dt = models.DateTimeField(auto_now=True)
#     updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#
# class Customer(models.Model):
#     code = models.CharField(max_length=10)
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     email = models.EmailField()
#     created_dt = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     updated_dt = models.DateTimeField(auto_now=True)
#     updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#
