from django.db import models

# ==================================================
# Model Mixins
# ==================================================

class BasicListModel(models.Model):

	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion

	class Meta:
		abstract=True
		ordering=['descripcion']


class SecuenciaBaseManager(models.Manager):

	def get_next(self):
		try:
			sec = self.get(id=1)
		except:
			sec = self.create()
		r = sec.numero
		sec.numero += 1
		sec.save()
		return r

	def alterar_secuencia(self, value):
		try:
			sec = self.get(id=1)
		except:
			sec = self.create()
		sec.nuemro = value
		sec.save()


class SecuenciaBase(models.Model):
	numero = models.IntegerField(default=1)
	objects = SecuenciaBaseManager()

	class Meta:
		abstract=True