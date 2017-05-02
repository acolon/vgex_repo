import sys
sys.path.append('/Users/arnaldo/code/modules/')
from ac_helpers.ascii import AsciiString

import csv
import re

TEMP_PATH = '/Users/arnaldo/temp/verbagas/'
SOURCE_FILE = TEMP_PATH + 'facturas.tsv'

'''
fields = ( 	'numero', 'fecha', 'condicion', 'cliente', 'galones', 
			'precio_galon', 'descuento', 'monto', 'vendedor', 
			'camion', 'chofer' )

def get_line(row):
	r = ''
	for field in fields:
		r += '{}:"{}", '.format(field, row[field])
	r = re.sub(', $', '', r)
	return r
'''

n = 0
with open(SOURCE_FILE, "r", encoding="Mac-Roman") as f:
	for row in csv.DictReader(f, delimiter='\t'):
		try:
			print(row)
			n += 1
		except:
			print()
			print('*'*50)
			print('Error en la factura {}'.format(row['numero']))
			line = ''
			for key in list(row.keys()):
				line += row[key] + '\t'
			line = re.sub('\t$', '', line)
			print(AsciiString(line))
			print('*'*50)
			print()
			break

print()
print('{} records loaded'.format(n))
