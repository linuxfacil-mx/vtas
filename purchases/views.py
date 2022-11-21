# from django.shortcuts import render
from django.forms import inlineformset_factory
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Supplier
from purchases.models import POHeader, PODetail


class POIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'purchases/po-index.html'
    # OrderFormSet = inlineformset_factory(
    # POHeader, PODetail, fields=('quantity',))
    # supplier = Supplier.objects.get(pk=1)
    # formset = OrderFormSet(instance=supplier)
    extra_context = {'title': 'Ordenes de Compra',
                     'inventory_active': True,
                     'po_active': True
                     # 'formset': formset
                     }
