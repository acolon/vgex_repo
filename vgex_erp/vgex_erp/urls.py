"""vgex_erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from .views import TempView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.auth.urls')), 
    url(r'^$', TempView.as_view(), name='vgex_root'),
    url(r'', include('clientes.urls', namespace='clientes')), 
    url(r'^params/', include('params.urls', namespace='params')), 
    url(r'^facturas/', include('facturas.urls', namespace='facturas')), 
    url(r'^ncf/', include('ncf.urls', namespace='ncf')), 
    url(r'^carga_manual/', include('rawdata.urls', namespace='rawdata')), 
]
