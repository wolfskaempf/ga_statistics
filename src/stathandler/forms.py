from django import forms
from .models import DummyData


class DummyForm(forms.ModelForm):
	class Meta:
		model = DummyData
		fields = ['number']
