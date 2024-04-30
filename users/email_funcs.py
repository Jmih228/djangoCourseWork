from django.core.mail import send_mail
from djangoCourseWork import settings
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def _send_mail_password(password, recipient_list):
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_list]
    )


def verification(request, user):
    context = {
        'user': user,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': token_generator.make_token(user)
    }
    message = render_to_string(
        'users/email_verification.html',
        context=context
    )

    send_mail(
        subject='Подтверждение почты',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
