from django.urls import path

from .views import IndexView, CustomLoginView, logout_view, StoreIndexView

urlpatterns = [
    path('', IndexView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('stores/', StoreIndexView.as_view(), name='stores'),
]
