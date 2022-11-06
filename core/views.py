# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


class LoginView(LoginView):
    template_name = "login.html"
    next_page = "dashboard"


class IndexView(TemplateView):
    template_name = "core/index.html"
