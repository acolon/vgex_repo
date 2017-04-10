from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Cliente, Contacto

# ==================================================
# Mixins
# ==================================================

class ClienteMixin(LoginRequiredMixin):
	model = Cliente
	success_url = reverse_lazy('clientes:list')


class EditClienteMixin(ClienteMixin):
	template_name = 'clientes/edit.html'
	fields = [ 'nombre', 'documento', 'direccion', 
		'telefono1', 'telefono2', 'fax', 'email', 
		'sector', 'vendedor', 'categoria', 'descuento',
		'dias_credito', 'notas' 
		]


class ContactoMixin(LoginRequiredMixin):
	model = Contacto

	def get_success_url(self):
		pass


class ContactoEditMixin(ContactoMixin):
	template_name = 'clientes/edit_contacto.html'
	fields = [
		'nombre', 
		]

# ==================================================
# Clientes Views
# ==================================================

class ClientesListView(ClienteMixin, ListView):
	template_name = 'clientes/list.html'


class ClientesCreateView(EditClienteMixin, CreateView):
	pass


class ClientesUpdateView(EditClienteMixin, UpdateView):
	pass


class ClientesDeleteView(ClienteMixin, DeleteView):
	template_name = 'clientes/delete.html'
	context_object_name = 'cliente'

# ==================================================
# Contactos Views
# ==================================================

class ContactosListView(ContactoMixin, ListView):
	pass


class ContactosCreateView(ContactoEditMixin, CreateView):
	pass


class ContactosUpdateView(ContactoEditMixin, UpdateView):
	pass


class ContactosDeleteView(ContactoMixin, DeleteView):
	pass
