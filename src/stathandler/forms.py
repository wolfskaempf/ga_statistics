from django import forms
from .models import DummyData


class DummyForm(forms.ModelForm):
	# This is a dummy form. It'll be removed once the real form is in place.
	class Meta:
		model = DummyData
		fields = ['number']
