from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Factura

# ==================================================
# Factura Mixin
# ==================================================

class FacturaMixin(LoginRequiredMixin):
	model = Factura
	context_object_name = 'factura'


# ==================================================
# ==================================================

class FacturasListView(FacturaMixin, ListView):
	template_name = 'facturas/list.html'
	context_object_name = 'facturas_list'


class FacturaDetailView(FacturaMixin, DetailView):
	template_name = 'facturas/detail.html'


class FacturaCreateView(FacturaMixin, CreateView):
	template_name = 'facturas/create.html'
	fields = [ 'fecha', 'cliente', 'galones', 'referencia' ]
	success_url = reverse_lazy('facturas:detail')
