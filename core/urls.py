from django.urls import path

from .views import IndexView, LoginView, logout_view

urlpatterns = [
    path('', IndexView.as_view(), name="dashboard"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
]
