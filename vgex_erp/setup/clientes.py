# This module deals with migrations

import sys
sys.path.append('/Users/arnaldo/code/modules/')
from ac_helpers.ascii import AsciiString

import csv
import re

from django.db import transaction
from django.utils.text import slugify

from clientes.models import Cliente, Sector, Categoria, Vendedor, Municipio
from clientes.forms import ClienteLoadForm


TEMP_PATH = '/Users/arnaldo/temp/verbagas/'
SOURCE_FILE = TEMP_PATH + 'clientes.tsv'
ERRORS_FILE = TEMP_PATH + 'clientes_errors.txt'


def set_support(row):

	mun = row['municipio'].strip().upper()
	Municipio.objects.get_or_create(descripcion=mun)

	sector = row['sector'].strip().title()
	Sector.objects.get_or_create(descripcion=sector)

	ven = row['vendedor'].strip().title()
	Vendedor.objects.get_or_create(nombre=ven)


def set_categoria():
	Categoria.objects.get_or_create(descripcion='N/D')


def get_sector(row):
	try:
		sector = Sector.objects.get(descripcion=row['sector'])
	except:
		return 0
	return sector.pk


def get_categoria():
	cat = Categoria.objects.all()[0]
	return cat.pk


def get_municipio(row):
	try:
		mun = Municipio.objects.get(descripcion=row['municipio'])
	except:
		return 0
	return mun.pk


def get_vendedor(row):
	try:
		ven = Vendedor.objects.get(nombre=row['vendedor'])
	except:
		return 0
	return ven.pk


def fix_row(row):
	for key in list(row.keys()):
		try:
			x = row[key]
			x = x.strip().title()
			row[key] = x
		except:
			pass
	row['nombre'] = row['nombre'].upper()
	row['municipio'] = row['municipio'].upper()
	try:
		row['descuento'] = int(row['descuento'])
	except:
		row['descuento'] = 0
	row['categoria'] = get_categoria()
	row['vendedor'] = get_vendedor(row)
	row['municipio'] = get_municipio(row)
	row['sector'] = get_sector(row)
	row['dias_credito'] = 7
	return row


def load_clientes():

	set_categoria()

	rows = []
	n = 0
	e = 0
	with open(SOURCE_FILE, "r", encoding="Mac-Roman") as f:
		print('Setting support data ...')
		for row in csv.DictReader(f, delimiter='\t'):
			set_support(row)
			row = fix_row(row)
			rows.append(row)
		print()

	with transaction.atomic():
		print('Loading clientes ...')
		for row in rows:
			print(row)
			print('-'*50)
			form = ClienteLoadForm(row)
			if form.is_valid():
				n += 1
				form.save()
				print('... saved')
			else:
				e += 1
				print('... error')
				print(form.errors)
				print()
			print()

	print()
	print('Finished loading clientes')
	print('{} rows loaded, {} errors found'.format(n, e))


def split_telefono(x):
	tel1 = x.strip()
	tel2 = ''
	if x.count('/'):
		arr = x.split('/')
		tel1 = arr[0]
		if len(arr) > 2:
			del arr[0]
			tel2 = ', '.join(arr)
		else:
			tel2 = arr[1]
	return tel1, tel2


def fix_cli_telefonos():
	print('Splitting Telefono Field')
	print()

	with transaction.atomic():
		for cliente in Cliente.objects.all():
			telefono = cliente.telefono1
			tel1, tel2 = split_telefono(telefono)
			cliente.telefono1 = tel1
			cliente.telefono2 = tel2
			cliente.save()
			print('Fixing "{}": {} splits into {} and {}'.format(
				cliente.nombre, telefono, tel1, tel2))


def set_cliente_slug():
	print('Slugifying ...')
	with transaction.atomic():
		for cliente in Cliente.objects.all():
			cliente.slug = slugify(cliente.nombre)
			cliente.save()
	print('... done')
	print()


def show_cliente_slug():
	for cliente in Cliente.objects.all():
		print(cliente.nombre)
		print(cliente.slug)
		print()


def show_cliente_dup():
	arr = []
	for cliente in Cliente.objects.all():
		if cliente.slug in arr:
			print('-'*50)
			print('Duplicate found ...')
			dups = Cliente.objects.filter(slug=cliente.slug)
			for dup in dups:
				print(dup.pk)
				print(dup.nombre)
				print(dup.slug)
				print('-')
			print()
		else:
			arr.append(cliente.slug)

def del_cli_dup():
	arr = []
	with transaction.atomic():
		for cliente in Cliente.objects.all():
			if cliente.slug in arr:
				print('Deleting cliente {}: {} ({})'.format(
					cliente.pk, cliente.nombre, cliente.slug
					))
				print()
				cliente.delete()
			else:
				arr.append(cliente.slug)
