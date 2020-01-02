from django import forms
from .validators import validate_url

class SubmitUrlForms(forms.Form):
	url = forms.CharField(label="", 
						validators=[validate_url],
						widget = forms.TextInput(attrs={
							"placeholder": "URL to Shorten...",
							"class": "form-control"
							})
		)
