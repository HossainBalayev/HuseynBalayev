from django import forms
from user.models import MY_USER
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your email'
    }))
    photo = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your phone number'
    }))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'
, 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    

    class Meta:
        model = MY_USER
        fields = ['photo', 'username','first_name', 'last_name', 'email','phone', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    }
        

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))