from django.contrib.auth import get_user_model
from django.db import models
from core.models import Store, Product, Supplier

User = get_user_model()


class POHeader(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    po_dt = models.DateField(auto_now_add=True)
    store_fk = models.ForeignKey(Store, on_delete=models.CASCADE)
    supplier_fk = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)


class PODetail(models.Model):
    po_fk = models.ForeignKey(POHeader, on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
