from django import forms
from .models import Cliente, Sector, Categoria, Vendedor, Municipio

class ClienteLoadForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [ 'nombre', 'vendedor', 'categoria', 'descuento', 
			'dias_credito', 'municipio', 'sector', 'direccion', 
			'referencia', 'documento', 'telefono1', 'observacion' ]


class ClienteForm(forms.ModelForm):

	def clean_nombre(self):
		nombre = self.cleaned_data['nombre']
		if 'nombre' in self.changed_data:
			id_cliente = self.instance.pk
			if not id_cliente:
				id_cliente = 0
			if Cliente.objects.slug_exists(nombre, id_cliente):
				msg  = 'El nombre de este cliente hace conflicto con otro, '
				msg += 'verifique que el cliente no exista o cambie el nombre'
				raise forms.ValidationError(msg)
		return nombre
		

	class Meta:
		model = Cliente
		fields = [ 'nombre', 'documento', 'categoria', 
			'vendedor', 
			'descuento',
			'dias_credito', 
			'municipio', 'sector', 'direccion', 
			'telefono1', 'telefono2', 'fax', 'email', 
			'observacion' 
			]
