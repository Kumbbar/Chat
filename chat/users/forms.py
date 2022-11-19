from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

