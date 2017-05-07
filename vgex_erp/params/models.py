from django.db import models
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

class PreciosManager(models.Manager):
	def get_precio(self, dia):
		precio = 0.0
		try:
			item = self.get(fecha=dia)
			precio = item.precio
		except ObjectDoesNotExist:
			precio = 0.0
		except:
			precio = 0.0
		return precio


class PrecioGalon(models.Model):
	fecha = models.DateField(unique=True)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	objects = PreciosManager()

	class Meta:
		ordering=['-fecha']


class Chofer(models.Model):
	nombre = models.CharField(max_length=100)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = [ 'nombre' ]
		verbose_name_plural = 'choferes'


class Camion(models.Model):
	ficha = models.CharField(max_length=20)
	capacidad = models.IntegerField(default=0)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.ficha

	class Meta:
		ordering = [ 'ficha' ]
		verbose_name_plural = 'camiones'