from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', 
		views.FacturasListView.as_view(), 
		name='list'), 

	url(r'^add/$', 
		views.FacturaCreateView.as_view(), 
		name='add'), 

	url(r'^(?P<pk>\d+)/detail/$', 
		views.FacturaDetailView.as_view(), 
		name='detail'), 
	

]