from django.db import models
from clientes.models import Cliente
from params.models import PrecioGalon 
import datetime

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


class Factura(models.Model):
	
	numero 			= models.IntegerField(default=0)
	cliente 		= models.ForeignKey(Cliente, related_name='facturas')
	fecha 			= models.DateField()
	galones 		= models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
	precio_galon 	= models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
	descuento_galon = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
	monto 			= models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
	dias_credito 	= models.IntegerField(default=0)
	fecha_vence 	= models.DateField()
	referencia 		= models.CharField(max_length=30, blank=True)

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
