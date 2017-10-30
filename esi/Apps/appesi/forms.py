from django import forms
#importando modelos
from .models import Cursomod
from .models import Tipocursomod
from .models import Tipopagomod

class CursoForm(forms.ModelForm):
	class Meta:
		model = Cursomod
		fields = '__all__'

class TipoCursoForm(forms.ModelForm):
	class Meta:
		model = Tipocursomod
		fields = '__all__'

class TipoPagoForm(forms.ModelForm):
	class Meta:
		model = Tipopagomod
		fields = '__all__'
		








