from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


# Login Form
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    widgets = {
        "username": forms.TextInput(attrs={"class": "login-design"}),
        "password": forms.TextInput(attrs={"class": "login-design"}),
    }


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        # fields = ['username','password1','password2','email']

    widgets = {
        "username": forms.TextInput(attrs={"class": "reg-user"}),
        "password1": forms.PasswordInput(attrs={"class": "form-control"}),
        "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        # 'email':forms.EmailInput(attrs={'class':"form-control"}),
    }
