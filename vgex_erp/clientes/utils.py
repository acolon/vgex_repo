from .models import Cliente, Sector, Categoria, Vendedor
from django.db import transaction

# ==================================================

class ClienteRow:

	_data = []
	def __init__(self, row):
		self._data = row.split('\t')

	@property
	def nombre(self):
		return self._data[0].strip().upper()

	@property
	def sector(self):
		return self._data[1].title().strip()

	@property
	def vendedor(self):
		return self._data[2].title().strip()

	@property
	def categoria(self):
		return self._data[3]

	@property
	def descuento(self):
		try:
			r = int(self._data[4])
		except:
			r = 0
		return r

	@property
	def dias_credito(self):
		try:
			r = int(self._data[5])
		except:
			r = 0
		return r

	@property
	def documento(self):
		return self._data[6].strip()

	@property
	def direccion(self):
		return self._data[7].strip().upper()

	@property
	def telefono1(self):
		return self._data[8].strip()

	@property
	def telefono2(self):
		return self._data[9].strip()

	@property
	def fax(self):
		return self._data[10].strip()

	@property
	def email(self):
		return self._data[11].strip()

	@property
	def observacion(self):
		return self._data[12].strip()

	@property
	def referencia(self):
		return self._data[13].strip()

	def show_info(self):
		print('-'*20)
		print(self.nombre)
		print(self.sector)
		print(self.vendedor)


class Loader:

	def read_file(self, file_path):
		# returns an array with the lines of the file
		arr = []
		print('Reading file {}'.format(file_path))
		with open(file_path, "r", encoding="Mac-Roman") as file:
			arr = [line.replace('\n', '') for line in file.readlines()]
		print('... {} records loaded'.format(len(arr)))
		print()
		return arr

	def start(self):

		cat, created = Categoria.objects.get_or_create(descripcion='n/d')

		with transaction.atomic():

			file = '/Users/arnaldo/temp/clientes_verbagas.txt'
			arr = self.read_file(file)
			for row in arr:
				obj = ClienteRow(row)

				print('Loading {}'.format(obj.nombre))

				sec, created = Sector.objects.get_or_create(descripcion=obj.sector)
				print('... sector: {}, {}'.format(sec.pk, sec.descripcion))

				ven, created = Vendedor.objects.get_or_create(nombre=obj.vendedor)
				print('... vendedor: {}, {}'.format(ven.pk, ven.nombre))

				cli = Cliente(
					nombre=obj.nombre,
					sector=sec,
					vendedor=ven,
					categoria=cat,
					descuento=obj.descuento,
					dias_credito=obj.dias_credito,
					documento=obj.documento,
					direccion=obj.direccion,
					telefono1=obj.telefono1,
					telefono2=obj.telefono2,
					observacion=obj.notas,
					referencia=obj.referencia
					)
				cli.save()

				print('... cliente: {}, {}'.format(cli.pk, cli.nombre))

				print()


