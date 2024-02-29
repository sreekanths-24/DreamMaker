from .models import *
from django import forms

class EventEditForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ['name', 'startdate', 'enddate', 'description', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'startdate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'enddate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'resize:none;'}),
            'user': forms.HiddenInput()
        }