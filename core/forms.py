from .models import *
from django import forms
PRIORITY_CHOICES = [
    ('Urgent/Important', 'Urgent/Important'),
    ('Not Urgent/Important', 'Not Urgent/Important'),
    ('Urgent/Not Important', 'Urgent/Not Important'),
    ('Not Urgent/Not Important', 'Not Urgent/Not Important')
]
class TodoEditForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'duedate', 'priority','dream']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-select'}, choices=PRIORITY_CHOICES),
            'dream': forms.HiddenInput()
        }

class AddDreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ['title','user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your dream here', 'required': True}),
            'user': forms.HiddenInput()
        }
class DreamAchievedForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ['achieved', 'user']
        widgets = {
            'achieved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'user': forms.HiddenInput()
        }