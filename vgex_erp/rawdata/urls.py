from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', 
		views.FacturasListView.as_view(), 
		name='facturas'), 

	url(r'^add/$', 
		views.FacturaCreateView.as_view(), 
		name='add_factura'), 

	url(r'^(?P<pk>\d+)/edit/$', 
		views.FacturaUpdateView.as_view(), 
		name='edit_factura'), 
	

	url(r'^(?P<pk>\d+)/delete/$', 
		views.FacturaDeleteView.as_view(), 
		name='delete_factura'), 
	

]