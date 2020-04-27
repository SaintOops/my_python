from django import forms
from django.forms import ModelForm

from .models import Paydata

class Paydataform (forms.ModelForm):
    class Meta:
        model= Paydata
        fields='__all__'
    