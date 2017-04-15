from django.db import models
from clientes.models import Cliente
from params.models import PrecioGalon 

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
	usuario = models.CharField(max_length=100)
	date_added = models.DateField(auto_now_add=True)

	objects = SecuenciaFacturaManager()


class Factura(models.Model):
	numero = models.IntegerField(default=0)
	cliente = models.ForeignKey(Cliente, related_name='facturas')
	fecha = models.DateField()
	galones = models.DecimalField(
		max_digits=7, 
		decimal_places=2,
		default=0.0)
	precio_galon = models.DecimalField(
		max_digits=5, 
		decimal_places=2, 
		default=0.0)
	descuento_galon = models.DecimalField(
		max_digits=4, 
		decimal_places=2, 
		default=0.0)
	monto = models.DecimalField(
		max_digits=9, 
		decimal_places=2, 
		default=0.0)
	dias_credito = models.IntegerField(default=0)
	fecha_vence = models.DateField()
	referencia = models.CharField(max_length=30, blank=True)

	def save(self, *args, **kwargs):
		if not self.pk:
			self.numero = SecuenciaFacturas.get_next()
			# self.descuento = self.cliente.descuento
			self.descuento = 0.0

		galones = self.galones
		precio = PrecioGalon.get_precio(self.fecha)
		descuento = self.descuento

		self.precio_galon = precio
		self.monto = galones * (precio - descuento)

		super(Factura, self).save(*args, **kwargs)
