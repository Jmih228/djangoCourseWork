from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import CustomUser
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from users.email_funcs import verification


class UserRegisterForm(UserCreationForm):

    class Meta:

        model = CustomUser
        fields = ('email', 'password1', 'password2')


class UserAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )
            if not self.user_cache.email_verificated:
                print(self.user_cache)
                verification(self.request, self.user_cache)
                raise ValidationError(
                    'Подтвердите почту чтобы войти в аккаунт',
                    code='invalid_login'
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserProfileForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()