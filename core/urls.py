from django.urls import path

from .views import IndexView, LoginView, logout_view, StoreIndexView

urlpatterns = [
    path('', IndexView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('stores/', StoreIndexView.as_view(), name='stores'),
]
