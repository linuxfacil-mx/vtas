from django.urls import reverse_lazy
from django.shortcuts import redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Store, Product, Supplier, Customer


class CustomLoginView(LoginView):
    template_name = "login.html"
    next_page = "dashboard"


def logout_view(request):
    logout(request)
    return redirect('login')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"
    extra_context = {'title': 'Dashboard', 'dashboard_active': True}


class StoreIndexView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'core/store-index.html'
    model = Store
    fields = ['code', 'name', 'address', 'phone']
    success_url = reverse_lazy('stores')
    extra_context = {'title': 'Tiendas',
                     'admin_active': True,
                     'stores_active': True}


class ProductIndexView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'core/product-index.html'
    model = Product
    fields = ['code', 'description']
    success_url = reverse_lazy('products')
    extra_context = {'title': 'Productos',
                     'admin_active': True,
                     'products_active': True}


class SupplierIndexView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'core/supplier-index.html'
    model = Supplier
    fields = ['code', 'name', 'address', 'phone', 'email']
    success_url = reverse_lazy('suppliers')
    extra_context = {'title': 'Proveedores',
                     'admin_active': True,
                     'suppliers_active': True}


class CustomerIndexView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'core/customer-index.html'
    model = Customer
    fields = ['code', 'name', 'address', 'phone', 'email']
    success_url = reverse_lazy('customers')
    extra_context = {'title': 'Clientes',
                     'admin_active': True,
                     'customers_active': True}
