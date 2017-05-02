import json
import re
from datetime import date, timedelta

TEMP_PATH = '/Users/arnaldo/temp/verbagas/'
SOURCE_FILE = TEMP_PATH + 'mic_precios.txt'
TARGET_FILE = TEMP_PATH + 'precios_glp.txt'

RANGO_FECHA = 'rangodevigencia'
GLP = 'glp'

MES_DICT = {
	'enero':1,
	'febrero':2,
	'marzo':3,
	'abril':4,
	'mayo':5,
	'junio':6,
	'julio':7,
	'agosto':8,
	'septiembre':9,
	'octubre':10,
	'noviembre':11,
	'diciembre':12
}

# ==================================================

def init_file(file_path):
	f = open(file_path, 'w', encoding='Mac-Roman')
	f.close()

def write_line(file_path, line):
	with open(file_path, 'a', encoding='Mac-Roman') as f:
		f.write(line + '\n')

def read_file(file_path):
	arr = []
	with open(file_path, "r", encoding="Mac-Roman") as file:
		arr = [line.replace('\n', '') for line in file.readlines()]
	return arr


# ==================================================

def get_ano(x):
	r = x[-4:]
	try:
		r = int(r)
	except:
		r = 0
	return r


def get_fechas_p1(x):

	ano = get_ano(x)

	pb = ' de \w+ de '
	m = re.search(pb, x)
	mes = m.group()
	mes = mes.strip()
	mes = re.sub('^de ', '', mes)
	mes = re.sub(' de$', '', mes)
	mes = MES_DICT.get(mes, 0)

	if not mes:
		print(x)
		raise ValueError

	pa = '^\d+ al \d+ de'
	m = re.search(pa, x)
	dias = m.group()
	dias = re.sub(' de$', '', dias)
	m = re.search('^\d+', dias)
	desde = int(m.group())
	m = re.search('\d+$', dias)
	hasta = int(m.group())
	da = date(ano, mes, desde)
	db = date(ano, mes, hasta)

	return (da, db)


def get_fechas_p2(x):

	da = date.today()
	db = date.today()

	x = x.replace(' al ', '\t')
	arr = x.split('\t')

	fa = arr[0]
	fb = arr[1]

	ano = get_ano(x)
	anox = ano

	p = ' de '
	a = fa.split(p)
	dia = int(a[0])

	mes = a[1].strip()
	if re.search(' \d{4}$', mes):
		anox = ano - 1 
		mes = mes[:-4].strip()

	mes = MES_DICT[mes]
	da = date(anox, mes, dia)

	m = re.search('^\d+', fb)
	dia = int(m.group())

	mes = re.sub('^\d+ ', '', fb)
	mes = re.sub('\d{4}$', '', mes).strip()
	mes = re.sub('^de ', '', mes)
	mes = re.sub(' de$', '', mes)
	mes = MES_DICT[mes]

	db = date(ano, mes, dia)

	return (da, db)


def convert_file():

	data = []
	with open(SOURCE_FILE) as f:
		text = f.read()
		text = text.lower()
		data = json.loads(text)

	data.reverse()
	ano_prev = 0
	arr = []

	init_file(TARGET_FILE)
	for item in data:

		rango = item[RANGO_FECHA]
		precio = item[GLP]

		ano = get_ano(rango)
		if ano:
			ano_prev = ano
		else:
			rango += ' de {}'.format(ano_prev)
			ano = ano_prev
		if ano < 2015:
			continue

		pa = '^del '
		if re.search(pa, rango):
			rango = re.sub(pa, '', rango)
		rango = rango.replace(' del ', ' de ')

		p = ' de \d{4}$'
		if not re.search(p, rango):
			rango = re.sub(' \d{4}$', ' de {}'.format(ano), rango)

		rango = rango.replace('oct.', 'octubre')
		rango = rango.replace('nov.', 'noviembre')
		rango = rango.replace('dic.', 'diciembre')

		pa = '^\d+ al \d+ de '
		pb = '^\d+ de '

		if re.search(pa, rango):
			da, db = get_fechas_p1(rango)
		elif re.search(pb, rango):
			da, db = get_fechas_p2(rango)

		d = da
		while d <= db:
			print('{}\t{}'.format(d, precio))
			x = '{}\t{}'.format(d, precio)
			write_line(TARGET_FILE, x)
			d = d + timedelta(days=1)

convert_file()