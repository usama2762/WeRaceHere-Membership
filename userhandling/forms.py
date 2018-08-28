from django.forms import ModelForm
from django import forms
from .models import Racer
class SignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Racer
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password','race_age',
                  'race_category','race_type','phone','city','state','street_address','zipcode',
                  'usac_number','brac_number']

class UpdateForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Racer
        fields = ['password']
