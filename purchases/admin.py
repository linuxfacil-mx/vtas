from django.contrib import admin

from purchases.models import POHeader, PODetail, POStatus

admin.site.register(POHeader)
admin.site.register(PODetail)
admin.site.register(POStatus)
