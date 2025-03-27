from django.urls import path
from . import views
from .views import LoginUserView, LogoutUserView, ResetPasswordConfirmView, ResetPasswordView, ChangePasswordView

app_name = 'authentication'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset-password-confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]