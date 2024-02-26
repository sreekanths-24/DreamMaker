from .models import *
from django import forms

class TodoEditForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'duedate']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }