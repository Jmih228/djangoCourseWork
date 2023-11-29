from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model
from users.models import CustomUser
from django.views.generic import CreateView, UpdateView
from django.views import View
from users.forms import UserRegisterForm, UserProfileForm, UserAuthenticationForm
from django.urls import reverse_lazy, reverse
from string import ascii_letters as letters, digits
from random import sample
from users.email_funcs import _send_mail_password, verification
from django.utils.http import urlsafe_base64_decode
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import LoginView


User = get_user_model()


class Verification(View):

    # def get(self, request, uid, token):
    #     user = self.get_user(uid)
    #
    #     if user is not None and token:
    #         user.is_verificated = True
    #         user.save()
    #         return redirect('user:login')
    #     return redirect('user:invalid_verify')

    def get(self, request, uid, token):
        user = self.get_user(uid)
        if user is not None and token_generator.check_token(user, token):
            user.email_verificated = True
            user.save()
            return redirect('users:login')
        return redirect('users:invalid_verify')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     return context_data

    @staticmethod
    def get_user(uid):
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(id=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


def get_new_password(request):
    password = ''.join(sample(letters + digits, 10))
    request.user.set_password(password)
    request.user.save()
    _send_mail_password(password, request.user.email)
    return redirect(reverse('users:logout'))


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:confirm_email')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            verification(self.request, self.object)
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect('users:login')


class MyLoginView(LoginView):

    form_class = UserAuthenticationForm
    template_name = 'users/login.html'
