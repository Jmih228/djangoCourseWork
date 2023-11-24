from django.core.mail import send_mail
from django.db.models import QuerySet
from mailing.models import Mail


def daily_func():
    mailings: QuerySet = Mail.objects.filter(status='enabled', send_frequency='daily')
    print(mailings)


def weekly_func():
    mailings: QuerySet = Mail.objects.filter(status='enabled', send_frequency='weekly')
    print(mailings)


def monthly_func():
    mailings: QuerySet = Mail.objects.filter(status='enabled', send_frequency='monthly')
    print(mailings)


# def main():
#
#     daily_func()
#     weekly_func()
#     monthly_func()
#
# main()
daily_func()
