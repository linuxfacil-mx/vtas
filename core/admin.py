from django.contrib import admin
from core.models import Store

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Store, StoreAdmin)
