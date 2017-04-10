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

