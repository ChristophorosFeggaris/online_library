from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'text', 'type': 'text', 'name': 'Username', 'placeholder': 'Username', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'text email', 'type': 'email', 'name': 'email', 'placeholder': 'Email', 'required': True}),
            'password1': forms.PasswordInput(attrs={'class': 'text', 'type': 'password', 'name': 'password', 'placeholder': 'Password', 'required': True}),
            'password2': forms.PasswordInput(attrs={'class': 'text w3lpass', 'type': 'password', 'name': 'password', 'placeholder': 'Confirm Password', 'required': True})
        }
