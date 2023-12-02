from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import *

app_name = MailingConfig.name

urlpatterns = [
    path('mailings', MailingListVeiw.as_view(), name='mailings'),
    path('create/', MailCreateView.as_view(), name='create_mailing'),
    path('view/<int:pk>', MailDetailView.as_view(), name='view'),
    path('update/<int:pk>', MailUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', MailDeleteView.as_view(), name='delete'),
    path('change_status/<int:pk>', change_status, name='change_status'),
    path('create_mail_message/', MessageCreateView.as_view(), name='message_create')
]
