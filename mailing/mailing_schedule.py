from django.core.mail import send_mail
from mailing.models import Mail, Message
import pytz
from django.conf import settings
from datetime import datetime, timedelta
from calendar import monthrange
import smtplib
from logs.models import Logs


def daily_func():
    mailings_queryset = Mail.objects.prefetch_related('clients').filter(status='started', send_frequency='daily')
    for mail in mailings_queryset:
        message = Message.objects.filter(mail_id=mail.id)
        try:
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in list(mail.clients.all())],
                fail_silently=False
            )
            mail.start_date = mail.start_date + timedelta(days=1)
            mail.status = 'completed'
            mail.save()
            status = 'Успешно'
        except smtplib.SMTPException as mail_exeption:
            status = 'Ошибка'
        finally:
            Logs.objects.create(
                last_mailing_time=mail.start_date,
                mail_status=status,
                mailmail_server_answering=str(mail_exeption),
            )


def weekly_func():
    mailings_queryset = Mail.objects.prefetch_related('clients').filter(status='started', send_frequency='weekly')
    for mail in mailings_queryset:
        message = Message.objects.filter(mail_id=mail.id)
        try:
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in list(mail.clients.all())],
                fail_silently=False
            )
            mail.start_date = mail.start_date + timedelta(days=7)
            mail.status = 'completed'
            mail.save()
            status = 'Успешно'
        except smtplib.SMTPException as mail_exeption:
            status = 'Ошибка'
        finally:
            Logs.objects.create(
                last_mailing_time=mail.start_date,
                mail_status=status,
                mailmail_server_answering=str(mail_exeption),
            )


def monthly_func():
    mailings_queryset = Mail.objects.prefetch_related('clients').filter(status='started', send_frequency='monthly')
    for mail in mailings_queryset:
        message = Message.objects.filter(mail_id=mail.id)
        try:
            send_mail(
                subject=message.subject,
                message=message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in list(mail.clients.all())],
                fail_silently=False
            )
            days = monthrange(mail.start_date.year, mail.end_date.month)[1]
            mail.start_date = mail.start_date + timedelta(days)
            mail.status = 'completed'
            mail.save()
            status = 'Успешно'
        except smtplib.SMTPException as mail_exeption:
            status = 'Ошибка'
        finally:
            Logs.objects.create(
                last_mailing_time=mail.start_date,
                mail_status=status,
                mailmail_server_answering=str(mail_exeption),
            )


def main():
    now = datetime.now().replace(tzinfo=pytz.UTC)

    mailings_query = Mail.objects.all()

    for mail in mailings_query:

        if mail.start_date < now < mail.end_date:
            mail.status = 'started'
            mail.save()

    daily_func()
    weekly_func()
    monthly_func()
