from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store.models import Product
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        
