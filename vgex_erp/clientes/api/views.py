from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView 
from rest_framework.response import Response

from ..models import Cliente
from .serializers import NombresClienteSerializer


class ClientesAPIView(APIView):
	permission_classes = ( IsAuthenticated, )

	def get(self, request, format=None):
		data = []
		if request.is_ajax():
			q = request.GET.get('term', '')
			clientes = Cliente.objects.filter(nombre__icontains=q)
			data = [cli.nombre for cli in clientes]
		else:
			data = 'fail'
		return Response(data)
