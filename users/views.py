from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = reverse_lazy('users:register')
