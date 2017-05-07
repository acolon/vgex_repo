from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import RawFactura


# ==================================================
# Mixins
# ==================================================

class FacturaMixin(LoginRequiredMixin):
	model = RawFactura
	success_url = reverse_lazy('rawdata:facturas')
	context_object_name = 'factura'


class FacturaEditMixin(FacturaMixin):
	template_name = 'rawdata/edit_factura.html'
	#form_class = FacturaForm
	fields = [ 'numero', 'fecha', 'condicion', 'cliente', 
			'galones', 'precio_galon', 'descuento', 
			'camion', 'chofer', 'valor_fiscal'
			]




# ==================================================
# Facturas Views
# ==================================================

class FacturasListView(FacturaMixin, ListView):
	template_name = 'rawdata/list_facturas.html'
	context_object_name = 'facturas'


class FacturaCreateView(FacturaEditMixin, CreateView):
	pass


class FacturaUpdateView(FacturaEditMixin, UpdateView):
	pass


class FacturaDeleteView(FacturaMixin, DeleteView):
	template_name = 'rawdata/delete_factura.html'
