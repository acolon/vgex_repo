from django.db import models
from core.models import BasicListModel

# ==================================================
# Model Mixins
# ==================================================


# ==================================================
# Choices
# ==================================================

TIPO_COMISION_CHOICES = (
	('p', 'Porcentual'),
	('v', 'Variable')
	)


# ==================================================
# Models
# ==================================================

class Vendedor(models.Model):

	nombre = models.CharField(max_length=50)
	documento = models.CharField(max_length=20, blank=True)
	salario = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	meta_galones = models.IntegerField(default=0)
	tipo_comision = models.CharField(max_length=1, choices=TIPO_COMISION_CHOICES, blank=True)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Vendedores'


class Categoria(BasicListModel):
	pass


class TipoContacto(BasicListModel):
	pass


class Sector(BasicListModel):
	class Meta:
		ordering = ['-descripcion']
		verbose_name_plural = 'Sectores'


class Cliente(models.Model):
	nombre 		 = models.CharField(max_length=100)
	sector 		 = models.ForeignKey(Sector, related_name='clientes')
	vendedor 	 = models.ForeignKey(Vendedor, related_name='clientes')
	categoria 	 = models.ForeignKey(Categoria, related_name='+')
	descuento 	 = models.IntegerField()
	dias_credito = models.IntegerField()
	documento 	 = models.CharField(max_length=20, blank=True)
	direccion 	 = models.CharField(max_length=250, blank=True)
	telefono1 	 = models.CharField(max_length=20, blank=True)
	telefono2 	 = models.CharField(max_length=20, blank=True)
	fax 		 = models.CharField(max_length=20, blank=True)
	email 		 = models.EmailField(max_length=100, blank=True)
	notas 		 = models.TextField(blank=True)
	referencia 	 = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.nombre


class Contacto(models.Model):
	nombre = models.CharField(max_length=100)
	tipo_contacto = models.ForeignKey(TipoContacto, related_name='+')
	cliente = models.ForeignKey(Cliente, related_name='contactos')
	cargo = models.CharField(max_length=100, blank=True)
	telefono = models.CharField(max_length=20, blank=True)
	celular = models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=100, blank=True)
