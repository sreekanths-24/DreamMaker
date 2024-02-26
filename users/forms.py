from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'phone', 'dob', 'designation', 'associated_with', 'twitter_link', 'linkedin_link', 'address']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'associated_with': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_link': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

# class AddMoreDetailsToProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'image', 'phone']
#         widgets = {
#             'bio': forms.Textarea(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'image': forms.FileInput(attrs={'class': 'form-control'}),
#         }