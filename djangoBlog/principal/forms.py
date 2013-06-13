from django import forms
from models import Alumnos

class AlumnosForm(forms.ModelForm):
	class Meta:
		model = Alumnos