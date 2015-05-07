from django import forms

from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    # Crispy Forms
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-1'
    helper.field_class = 'col-lg-3 input-lg'
    helper.layout = Layout(
        Field('username'),
        Field('password'),
        Submit('submit', 'Login', css_class='btn-default btn-lg col-lg-4 col-xs-12'),
    )
