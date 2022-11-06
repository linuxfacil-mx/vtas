from django.shortcuts import redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Store


class LoginView(LoginView):
    template_name = "login.html"
    next_page = "dashboard"


def logout_view(request):
    logout(request)
    return redirect('login')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"
    extra_context = {'title': 'Dashboard', 'dashboard_active': True}


class StoreIndexView(ListView):
    template_name = 'core/store-index.html'
    model = Store
    extra_context = {'title': 'Tiendas',
                     'admin_active': True,
                     'stores_active': True}
