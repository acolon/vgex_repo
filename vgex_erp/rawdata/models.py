from django.db import models
from params.models import Camion, Chofer

# ==================================================
# Choices
# ==================================================

CH_CONDICION = (
	(1, 'Contado'),
	(2, 'Crédito')
	)


# ==================================================
# models
# ==================================================

class RawFactura(models.Model):
	numero 			= models.IntegerField()
	fecha 			= models.DateField()
	condicion		= models.IntegerField(choices=CH_CONDICION)
	cliente 		= models.CharField(max_length=100)
	galones 		= models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
	precio_galon 	= models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
	descuento		= models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
	monto 			= models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
	camion 			= models.ForeignKey(Camion, related_name='+')
	chofer 			= models.ForeignKey(Chofer, related_name='+')
	valor_fiscal	= models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		galones = self.galones
		precio = self.precio_galon
		descuento = self.descuento
		self.monto = ( galones * precio ) - descuento
		super(RawFactura, self).save(*args, **kwargs)

	class Meta:
		ordering = ( '-fecha', )