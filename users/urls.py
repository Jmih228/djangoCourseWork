from django.urls import path
from users.apps import UsersConfig
from users.views import *
from django.views.generic import TemplateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/new_password/', get_new_password, name='new_password'),
    path('verification/<uid>/<token>/', Verification.as_view(), name='verification'),
    path('confirm_email', TemplateView.as_view(template_name='users/confirm_email.html'),
         name='confirm_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify')
]
