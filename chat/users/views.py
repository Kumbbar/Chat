from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from chat.settings import LOGIN_REDIRECT_URL


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy(LOGIN_REDIRECT_URL)


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = reverse_lazy(LOGIN_REDIRECT_URL)


class LogoutUser(LogoutView):
    template_name = 'users/logged_out.html'
