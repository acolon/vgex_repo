import uuid as uuid_lib
from django.db import models
from django.utils.text import slugify
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
# Managers
# ==================================================

class ClienteManager(models.Manager):
	def slug_exists(self, cur_nombre, cur_id=0):
		cur_slug = slugify(cur_nombre)
		qs = self.filter(slug=cur_slug).exclude(id=cur_id)
		if qs.count():
			return True
		else:
			return False


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
		ordering=['nombre']


class Categoria(BasicListModel):
	pass


class TipoContacto(BasicListModel):
	pass


class Sector(BasicListModel):
	class Meta:
		ordering = ['descripcion']
		verbose_name_plural = 'Sectores'


class Municipio(BasicListModel):
	class Meta:
		ordering = ['descripcion']


class Cliente(models.Model):
	'''
	To do:
	- create a slug automatically
	- change the slug when the name changes
	'''
	nombre 		 = models.CharField(max_length=100)
	slug		 = models.SlugField(max_length=100, unique=True)
	uuid		 = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
	vendedor 	 = models.ForeignKey(Vendedor, related_name='clientes')
	categoria 	 = models.ForeignKey(Categoria, related_name='+')
	descuento 	 = models.IntegerField()
	dias_credito = models.IntegerField()
	municipio  	 = models.ForeignKey(Municipio, related_name='+')
	sector 		 = models.ForeignKey(Sector, related_name='+')
	direccion 	 = models.CharField(max_length=250, blank=True)
	documento 	 = models.CharField(max_length=20, blank=True)
	telefono1 	 = models.CharField(max_length=35, blank=True)
	telefono2 	 = models.CharField(max_length=35, blank=True)
	fax 		 = models.CharField(max_length=20, blank=True)
	email 		 = models.EmailField(max_length=100, blank=True)
	observacion	 = models.TextField(blank=True)
	referencia 	 = models.CharField(max_length=20, blank=True)

	_old_nombre = ''

	objects = ClienteManager()

	def __init__(self, *args, **kwargs):
		super(Cliente, self).__init__(*args, **kwargs)
		self._old_nombre = self.nombre

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if self.nombre != self._old_nombre:
			self.slug = slugify(self.nombre)
			self._old_nombre = self.nombre
		if self.nombre != self.nombre.upper():
			self.nombre = self.nombre.upper()
		super(Cliente, self).save(*args, **kwargs)

	class Meta:
		ordering=['nombre']


class Contacto(models.Model):
	nombre = models.CharField(max_length=100)
	tipo_contacto = models.ForeignKey(TipoContacto, related_name='+')
	cliente = models.ForeignKey(Cliente, related_name='contactos')
	cargo = models.CharField(max_length=100, blank=True)
	telefono = models.CharField(max_length=20, blank=True)
	celular = models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=100, blank=True)


class NotasCliente(models.Model):
	cliente = models.ForeignKey(Cliente, related_name='notas')
	fecha = models.DateField()
	nota = models.TextField()
	created_by = models.CharField(max_length=50, blank=True)
	created_at = models.DateField(auto_now_add=True)
	estatus = models.IntegerField(choices=(
			(1, 'Vigente'),
			(2, 'Resuelta'),
			(3, 'Descartada')
		))

