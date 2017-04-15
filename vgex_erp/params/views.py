from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import PrecioGalon

# ==================================================
# Mixins
# ==================================================

class PreciosMixin(LoginRequiredMixin):
	model = PrecioGalon
	success_url = reverse_lazy('params:precios_list')
	context_object_name = 'precio_galon'


class EditPreciosMixin(PreciosMixin):
	template_name = 'params/precios_edit.html'
	fields = [ 'fecha', 'precio' ]


# ==================================================
# Precios x Galon Views
# ==================================================

class PreciosListView(PreciosMixin, ListView):
	template_name = 'params/precios_list.html'
	context_object_name = 'precios_list'


class PreciosCreateView(EditPreciosMixin, CreateView):
	pass


class PreciosUpdateView(EditPreciosMixin, UpdateView):
	pass


class PreciosDeleteView(PreciosMixin, DeleteView):
	template_name = 'params/precios_delete.html'
