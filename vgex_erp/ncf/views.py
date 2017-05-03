from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Ncf


# ==================================================
# Mixins
# ==================================================

class NcfMixin(LoginRequiredMixin):
	model = Ncf
	success_url = reverse_lazy('ncf:list')


class NcfEditMixin(NcfMixin):
	template_name = 'ncf/edit.html'
	fields = [ 'primer', 'ultimo' ]


# ==================================================
# Ncf Views
'''
There should be only List and Create views, upates, and deletion should be
controlled if at all possible
'''
# ==================================================

class NcfListView(NcfMixin, ListView):
	template_name = 'ncf/list.html'


class NcfCreateView(NcfEditMixin, CreateView):
	pass


