from .models import PrecioGalon
from django.db import transaction
from datetime import datetime

# ==================================================

class PrecioRow:

	_data = []
	def __init__(self, row):
		self._data = row.split('\t')

	@property
	def fecha(self):
		r = datetime.strptime(self._data[0], '%Y-%m-%d').date()
		return r

	@property
	def precio(self):
		return float(self._data[1])


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

		with transaction.atomic():

			file = '/Users/arnaldo/temp/verbagas/precios_glp.txt'
			arr = self.read_file(file)
			for row in arr:
				obj = PrecioRow(row)

				print('Loading {}'.format(obj.fecha))

				item = PrecioGalon(fecha=obj.fecha, precio=obj.precio)
				item.save()

				print('... registro: {}, {}, {}'.format(
					item.pk, item.fecha, item.precio))

				print()


