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
        fields = ['title', 'description', 'duedate', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-select'}, choices=PRIORITY_CHOICES)
        }