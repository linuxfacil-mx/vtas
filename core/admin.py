from django.contrib import admin
from core.models import Store, Product, Supplier, Customer

# Register your models here.

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
