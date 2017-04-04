from datetime import date, timedelta, datetime

def date_to_string(x):
	return x.isoformat().replace('-','')

def string_to_date(string_date):

	x = string_date

	if type(x) is str:
		pass
	elif type(x) is int:
		x = str(x)
	else:
		x = ''

	if x.count('-'):
		x = x.replace('-','')

	if len(x) == 8:
		pass
	elif len(x) == 6:
		x += '01'
	elif len(x) == 4:
		x += '0101'
	else:
		x = ''

	if x == '':
		r = None
	else:
		y = int(x[0:4])
		m = int(x[4:6])
		d = int(x[6:8])
		try:
			r = date(y,m,d)
		except:
			r = date.today() - timedelta(hours=4)
			# the use of timedelta here is to adjust to UTC-4

	return r


class DateParserBase:

	_date = None
	_prev_date = None
	_next_date = None
	_first_day = None # first day of month
	_last_day = None # last day of month
	_prev_month = None # first day of previous month
	_next_month = None # first day of next month

	@property
	def date(self):
		return self._date

	@property
	def prev_date(self):
		return self._prev_date
	
	@property
	def next_date(self):
		return self._next_date
	
	@property
	def first_day(self):
		return self._first_day
	
	@property
	def last_day(self):
		return self._last_day
	
	@property
	def prev_month(self):
		return self._prev_month
	
	@property
	def next_month(self):
		return self._next_month

	@property
	def month_name(self):
		return self._date.strftime('%B')
	

	def __init__(self, date_arg):

		if type(date_arg) is date:
			self._date = date_arg
		else:
			self._date = string_to_date(date_arg)

		if self._date:
			self.set_related_dates()
		else:
			self.clear_related_dates()

	def to_string(self):
		print('date:       {}'.format(self._date))
		print('prev day:   {}'.format(self._prev_date))
		print('next day:   {}'.format(self._next_date))
		print('first day:  {}'.format(self._first_day))
		print('last day:   {}'.format(self._last_day))
		print('prev month: {}'.format(self._prev_month))
		print('next month: {}'.format(self._next_month))

	def clear_related_dates(self):
		self._prev_date = None
		self._next_date = None
		self._first_day = None
		self._last_day = None
		self._prev_month = None
		self._next_month = None

	def set_related_dates(self):

		ONE_DAY = timedelta(days=1) # constant for date operations
		d = self._date # object's date

		fd = d.replace(day=1) # first day of month

		# get last day of month (ld)

		if d.day >= 28:
			ld = d
		else:
			ld = d.replace(day=28)

		x = d.month
		y = d.month

		while x == y:
			ld = ld + ONE_DAY
			y = ld.month

		ld = ld - ONE_DAY # ld = last day of month

		pm = (fd - ONE_DAY).replace(day=1) # previous month (first day)
		nm = (ld + ONE_DAY).replace(day=1) # next month (first day)
		pd = d - ONE_DAY # previous day
		nd = d + ONE_DAY # next day

		self._prev_date = pd
		self._next_date = nd
		self._first_day = fd
		self._last_day = ld
		self._prev_month = pm
		self._next_month = nm 


class DateArgs:

	_parser = None

	@property
	def date(self):
		r = ''
		x = self._parser.date
		if x:
			r = date_to_string(x)
		return r
	
	@property
	def prev_date(self):
		r = ''
		x = self._parser.prev_date
		if x:
			r = date_to_string(x)
		return r
	
	@property
	def next_date(self):
		r = ''
		x = self._parser.next_date
		if x:
			r = date_to_string(x)
		return r
	
	@property
	def first_day(self):
		r = ''
		x = self._parser.first_day
		if x:
			r = date_to_string(x)
		return r

	@property
	def last_day(self):
		r = ''
		x = self._parser.last_day
		if x:
			r = date_to_string(x)
		return r
	
	@property
	def prev_month(self):
		r = ''
		x = self._parser.prev_month
		if x:
			r = date_to_string(x)[0:6]
		return r
	
	@property
	def next_month(self):
		r = ''
		x = self._parser.next_month
		if x:
			r = date_to_string(x)[0:6]
		return r

	@property
	def month_name(self):
		r = ''
		x = self._parser.date 
		if x:
			r = x.strftime('%B')
		return r

	def __init__(self, date_arg):
		self._parser = DateParserBase(date_arg)

	def to_string(self):
		print('date:       {}'.format(self.date))
		print('prev day:   {}'.format(self.prev_date))
		print('next day:   {}'.format(self.next_date))
		print('first day:  {}'.format(self.first_day))
		print('last day:   {}'.format(self.last_day))
		print('prev month: {}'.format(self.prev_month))
		print('next month: {}'.format(self.next_month))
		print('month name: {}'.format(self.month_name))


class DateParser(DateParserBase):

	_args = None

	@property
	def args(self):
		return self._args

	def __init__(self, date_arg):
		super(DateParser, self).__init__(date_arg)
		self._args = DateArgs(date_arg)

