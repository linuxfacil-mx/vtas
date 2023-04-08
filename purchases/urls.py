from django.urls import path

from purchases.views import POIndexView, PONewView

urlpatterns = [
    path('', POIndexView.as_view(), name='PO_index'),
    path('new/', PONewView.as_view(), name='PO_new'),
]
