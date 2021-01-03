from django import forms
from django.forms import ModelForm
from .models import *

class LabForm(ModelForm):
    class Meta:
        model = Lab
        fields = ['name']
        # fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
