from django.shortcuts import redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(LoginView):
    template_name = "login.html"
    next_page = "dashboard"


def logout_view(request):
    logout(request)
    return redirect('login')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"
