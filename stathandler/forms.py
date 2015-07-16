from django import forms


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton


from .models import CommitteeStatistic, Committee


class CommitteeStatisticForm(forms.ModelForm):
	# This is the form which is commonly used by chairs to submit data about the most recent point to the database. Data entered into this form will automatically show up on the screen during GA.
	class Meta:
		model = CommitteeStatistic
		fields = ['committee', 'pointResume']
