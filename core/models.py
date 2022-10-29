from django.db import models


class Store(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    created_dt = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    updated_dt = models.DateTimeField(auto_now=True)


class Supplier(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    created_dt = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    updated_dt = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    created_dt = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    updated_dt = models.DateTimeField(auto_now=True)
