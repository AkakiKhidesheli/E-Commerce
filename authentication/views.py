from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.models import CATEGORY_CHOICES


# Create your views here.

class RegisterUserView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('authentication:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class LoginUserView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('core:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class LogoutUserView(LogoutView):
    next_page = reverse_lazy('core:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class ResetPasswordView(PasswordResetView):
    template_name = 'authentication/reset_password.html'
    email_template_name = 'authentication/password_reset_email.html'
    success_url = reverse_lazy('authentication:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/reset_password_confirmation.html'
    success_url = reverse_lazy('authentication:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class ChangePasswordView(PasswordChangeView):
    template_name = 'authentication/change_password.html'
    success_url = reverse_lazy('core:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context