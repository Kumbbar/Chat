from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from chat.settings import LOGIN_REDIRECT_URL
from channels.http import AsgiRequest


class RegisterUser(View):
    def get(self, request: AsgiRequest):
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request: AsgiRequest):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            form.login_new_user(request)
            return redirect(LOGIN_REDIRECT_URL)
        return render(request, 'users/register.html', {'form': form})



class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = reverse_lazy(LOGIN_REDIRECT_URL)


class LogoutUser(LogoutView):
    template_name = 'users/logged_out.html'
