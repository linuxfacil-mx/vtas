from django.contrib import admin

from purchases.models import POHeader, PODetail

admin.site.register(POHeader)
admin.site.register(PODetail)
