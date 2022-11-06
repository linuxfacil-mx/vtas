# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(LoginView):
    template_name = "login.html"
    next_page = "dashboard"


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"
