from django.db import models


class NcfManager(models.Manager):

	def get_next(self):
		ncf = self.get_current()
		if ncf:
			ncf.secuencia += 1
			ncf.save()
			r = ncf.secuencia
		else:
			r = 0
		return r

	def get_current(self):
		qs = self.filter(activo=True)
		if qs.count():
			return qs[0]
		else:
			return None

	def none_active(self):
		ncf = self.get_current()
		if ncf:
			return False
		else:
			return True


class Ncf(models.Model):
	primer = models.IntegerField()
	ultimo = models.IntegerField()
	secuencia = models.IntegerField(default=0)
	activo = models.BooleanField(default=False)

	objects = NcfManager()

	def save(self, *args, **kwargs):
		if Ncf.objects.none_active():
			self.activo = True
		super(Ncf, self).save(*args, **kwargs)

	class Meta:
		ordering = ( 'primer', )