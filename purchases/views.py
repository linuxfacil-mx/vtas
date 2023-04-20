from django.urls import reverse_lazy
# from django.forms import inlineformset_factory
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# from core.models import Supplier
from purchases.models import POStatus

class POStatusCreateView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'purchases/po-status.html'
    model = POStatus
    fields = ['code', 'status', 'seq']
    success_url = reverse_lazy('po_status')
    extra_context = {'title': 'Status - Ordenes de Compra', 
                     'admin_active': True, 
                     'po_status_active': True}

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

class PONewView(LoginRequiredMixin, TemplateView):
    template_name = 'purchases/po-new.html'
