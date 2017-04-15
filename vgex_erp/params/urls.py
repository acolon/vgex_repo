from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^precios/$', 
		views.PreciosListView.as_view(), 
		name='precios_list'), 

	url(r'^precios/add/$', 
		views.PreciosCreateView.as_view(), 
		name='precio_add'), 

	url(r'^precios/(?P<pk>\d+)/edit/$', 
		views.PreciosUpdateView.as_view(), 
		name='precio_edit'), 

	url(r'^precios/(?P<pk>\d+)/delete/$', 
		views.PreciosDeleteView.as_view(), 
		name='precio_delete'), 

]