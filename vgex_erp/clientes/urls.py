from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^clientes/$', 
		views.ClientesListView.as_view(), 
		name='list'), 

	url(r'^clientes/add/$', 
		views.ClientesCreateView.as_view(), 
		name='add'), 

	url(r'^clientes/(?P<pk>\d+)/edit/$', 
		views.ClientesUpdateView.as_view(), 
		name='edit'), 

	url(r'^clientes/(?P<pk>\d+)/delete/$', 
		views.ClientesDeleteView.as_view(), 
		name='delete'), 

	#url(r'^vendedores/$', views.VendedoresListView.as_view(), name='vendedores_list'), 


	]
"""
	url(r'^income/add/$', views.IncomeCategoryCreateView.as_view(), 
		name='add_income'), 
	url(r'^income/(?P<pk>\d+)/edit/$', 
		views.IncomeCategoryUpdateView.as_view(), 
		name='edit_income'), 
	url(r'^income/(?P<pk>\d+)/delete/$', 
		views.IncomeCategoryDeleteView.as_view(), 
		name='delete_income'), 

	url(r'^expense/$', views.ExpenseCategoryListView.as_view(), 
		name='expense'), 
	url(r'^expense/add/$', views.ExpenseCategoryCreateView.as_view(), 
		name='add_expense'), 
	url(r'^expense/(?P<pk>\d+)/edit/$', 
		views.ExpenseCategoryUpdateView.as_view(), 
		name='edit_expense'), 
	url(r'^expense/(?P<pk>\d+)/delete/$', 
		views.ExpenseCategoryDeleteView.as_view(), 
		name='delete_expense'), 
"""
