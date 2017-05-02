from django.db import models
from clientes.models import Cliente
from params.models import PrecioGalon, Chofer, Camion
import datetime


# ==================================================
# Choices
# ==================================================

CONDICION_FACTURA_CHOICES = (
	(1, 'Contado'),
	(2, 'Crédito')
	)

# ==================================================
# Managers
# ==================================================

class SecuenciaFacturaManager(models.Manager):
	def get_next(self):
		item = self.create()
		item.save()
		return item.pk


# ==================================================
# Models
# ==================================================

class SecuenciaFacturas(models.Model):
	date_added = models.DateField(auto_now_add=True)
	objects = SecuenciaFacturaManager()


class NewFactura(models.Model):
	fecha = models.DateField()
	cliente = models.CharField(max_length=100)
	galones = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
	condicion = models.IntegerField(choices=CONDICION_FACTURA_CHOICES)
	fiscal = models.BooleanField(default=False)

	def get_cliente(self):
		try:
			cliente = Cliente.objects.get(nombre=self.cliente)
		except:
			cliente = None
		return cliente

	def save(self, *args, **kwargs):
		if self.pk:
			# this should never update, but just in case
			pass
		else:
			cliente = self.get_cliente()
			if cliente:
				dias_credito = self.cliente.dias_credito
				fecha_vence = self.fecha + datetime.timedelta(days=dias_credito)
				numero = SecuenciaFacturas.objects.get_next()
				descuento = self.cliente.descuento
				galones = self.galones
				precio = PrecioGalon.objects.get_precio(self.fecha)
				monto = galones * (precio - descuento)


			# get numero
			# get dias credito
			# calculate fecha vence
			# get precio galon
			#


class Factura(models.Model):

	numero 			= models.IntegerField(default=0)
	fecha 			= models.DateField()
	condicion		= models.IntegerField(choices=CONDICION_FACTURA_CHOICES)
	cliente 		= models.ForeignKey(Cliente, related_name='facturas')
	galones 		= models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
	precio_galon 	= models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
	descuento		= models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
	monto 			= models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
	fecha_vence 	= models.DateField()
	camion 			= models.ForeignKey(Camion, related_name='+')
	chofer 			= models.ForeignKey(Chofer, related_name='+')
	referencia 		= models.CharField(max_length=30, blank=True)
	numero_fiscal	= models.CharField(max_length=50, blank=True)

	def save(self, *args, **kwargs):

		if not self.pk:

			dias_credito = self.cliente.dias_credito
			fecha_vence = self.fecha + datetime.timedelta(days=dias_credito)

			self.numero = SecuenciaFacturas.objects.get_next()
			self.descuento_galon = self.cliente.descuento
			self.dias_credito = dias_credito
			self.fecha_vence = fecha_vence

		galones = self.galones
		precio = PrecioGalon.objects.get_precio(self.fecha)
		descuento = self.descuento_galon

		self.precio_galon = precio
		self.monto = galones * (precio - descuento)

		super(Factura, self).save(*args, **kwargs)
