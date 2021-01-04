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

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'result': forms.Select(attrs={'class': 'form-control'}),
        }

class DataTrainingForm(ModelForm):
    class Meta:
        model = TrainingValue
        fields = '__all__'
        widgets = {
            'attribute_id': forms.Select(attrs={'class': 'form-control'}),
            'training_id': forms.Select(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control','step': '0.01'}),
        }
