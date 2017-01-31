from django import forms
from django.contrib.auth.models import User
from . import models
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Haslo")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
        'username': 'Nazwa uzytkownika'
        }

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['gender','firstname','lastname']
        labels = {
          'gender': 'Plec',
          'firstname': 'Imie',
          'lastname': 'Nazwisko'
        }
