from django.db import models
from mailing.models import Mail

class Logs(models.Model):

    last_mailing_time = models.DateTimeField(verbose_name='Дата последней рассылки')
    mail_status = models.CharField(max_length=50, verbose_name='Статус попытки')
    mail_server_answer = models.CharField(max_length=150, verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f'{self.mail_status}, {self.mail_server_answer}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
