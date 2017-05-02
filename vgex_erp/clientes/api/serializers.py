from rest_framework import serializers
from ..models import Cliente


class NombresClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = [ 'nombre' ]