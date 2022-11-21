from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('purchases/', include('purchases.urls')),
    path('admin/', admin.site.urls),
]
