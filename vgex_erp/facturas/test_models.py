from django.test import TestCase
from .models import Factura
from clientes.models import Cliente, Sector, Categoria, Vendedor
from params.models import PrecioGalon
from datetime import date, timedelta

# ==================================================

class FacturaModelTests(TestCase):

	def setUp(self):

		sec = Sector(descripcion='Naco')
		sec.save()

		cat = Categoria(descripcion='Catering')
		cat.save()

		ven = Vendedor(nombre='Arnaldo', documento='001', salario=250000.0,
			meta_galones=1000, tipo_comision='v')
		ven.save()

		cli = Cliente(nombre='VIP Catering Gourmet', sector=sec, 
			vendedor=ven, categoria=cat, descuento=-4, dias_credito=45)
		cli.save()

		precio = PrecioGalon(fecha=date(2017,2,14), precio=100.5)
		precio.save()


	def test_new_factura(self):
		"""
		Tests that all fields are properly populated, given that several
		fields depend on models SecuenciaFactura, Cliente and PrecioGalon
		"""

		cli = Cliente.objects.get(pk=1)

		print()
		print('Cliente ........ : {}, {}'.format(cli.pk, cli.nombre))
		print('Sector ......... : {}'.format(cli.sector.descripcion))
		print('Categoria ...... : {}'.format(cli.categoria.descripcion))
		print('Descuento ...... : {}'.format(cli.descuento))
		print('Dias Credito ... : {}'.format(cli.dias_credito))
		print()

		item = Factura(cliente=cli, fecha=date(2017,2,14), 
				galones=70, referencia='1025')
		item.save()

		print()
		print('Numero factura ... : {}'.format(item.numero))
		print('Cliente Id ....... : {}'.format(item.cliente.pk))
		print('Precio Galon ..... : {}'.format(item.precio_galon))
		print('Descuento Galon .. : {}'.format(item.descuento_galon))
		print('Monto Factura .... : {}'.format(item.monto))
		print('Dias Credito ..... : {}'.format(item.dias_credito))
		print('Fecha Vence ...... : {}'.format(item.fecha_vence))
		print()

		self.assertEqual(item.cliente.pk, 1)
		self.assertEqual(item.precio_galon, 100.5)
		self.assertEqual(item.descuento_galon, -4)
		self.assertEqual(item.dias_credito, 45)
