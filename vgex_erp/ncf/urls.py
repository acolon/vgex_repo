from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', 
		views.NcfListView.as_view(), 
		name='list'), 

	url(r'^add/$', 
		views.NcfCreateView.as_view(), 
		name='add'), 
	

]