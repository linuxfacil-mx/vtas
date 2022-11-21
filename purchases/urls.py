from django.urls import path

from purchases.views import POIndexView

urlpatterns = [
    path('', POIndexView.as_view(), name='PO_index'),
]
