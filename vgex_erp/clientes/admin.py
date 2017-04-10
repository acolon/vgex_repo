from django.contrib import admin

from .models import Vendedor, Categoria, TipoContacto, Sector

# ==================================================
# Admin Mixins
# ==================================================

class BasicListAdmin(object):
	list_display = [ 'descripcion' ]
	search_fields = [ 'descripcion' ]


# ==================================================
# Admin Registrations
# ==================================================

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'documento', 'salario', 'meta_galones', 'tipo_comision' ]
	search_fields = ['nombre']


@admin.register(Categoria)
class CategoriaAdmin(BasicListAdmin, admin.ModelAdmin):
	pass

@admin.register(TipoContacto)
class TipoContactoAdmin(BasicListAdmin, admin.ModelAdmin):
	pass

@admin.register(Sector)
class SectorAdmin(BasicListAdmin, admin.ModelAdmin):
	pass
