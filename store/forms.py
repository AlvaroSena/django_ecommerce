from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CreateNewCustomer(forms.Form):
	name = forms.CharField(label='Name', max_length=128)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Customer
		fields = ['name', 'email', 'password']