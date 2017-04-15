from django.contrib import admin
from .models import Chofer, Camion

@admin.register(Chofer)
class ChoferAdmin(admin.ModelAdmin):
	list_display  = [ 'nombre' ]
	search_fields = [ 'nombre' ]


@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
	list_display  = [ 'ficha', 'capacidad' ]
	search_fields = [ 'ficha' ]
