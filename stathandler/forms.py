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


# class CommitteeStatisticFormNew(forms.Form):
#     # This is the form a user fills out to log in
#     committee = forms.ForeignKey
#     pointResume = forms.TextField
#
#
#     # Crispy Forms. This defines what the form should look like when displayed. This is specific to Bootstrap 3
#     helper = FormHelper()
#     helper.form_class = 'form-horizontal'
#     helper.label_class = 'col-lg-1'
#     helper.field_class = 'col-lg-3 input-lg'
#     helper.layout = Layout(
#         Field('committee'),
#         Field('pointResume'),
#         Submit('submit', 'Submit', css_class='btn-default btn-lg col-lg-4 col-xs-12'),
#     )
