from django.db import models
from djangoCourseWork import settings
from clients.models import Client

class Mail(models.Model):

    SEND_CHOICES = (
        ('daily', 'раз в день'),
        ('weekly', 'раз в неделю'),
        ('monthly', 'раз в месяц'),
    )
    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
        ('blocked', 'Заблокирована')
    )
    title = models.CharField(max_length=100, verbose_name='Название рассылки')
    start_date = models.DateTimeField(verbose_name="Дата начала рассылки", null=True, blank=True)
    end_date = models.DateTimeField(verbose_name="Дата окончания рассылки", null=True, blank=True)
    send_time = models.TimeField(verbose_name="Время длительности рассылки")
    send_frequency = models.CharField(max_length=10, choices=SEND_CHOICES, verbose_name="Частота рассылки")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='created', verbose_name="Статус рассылки")
    clients = models.ManyToManyField(Client, verbose_name="Клиенты", related_name="mailings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                             verbose_name="Пользователь")

    def __str__(self):
        return self.title


class Message(models.Model):

    subject = models.CharField(max_length=255, verbose_name='тема')
    body = models.TextField(verbose_name='сообщение')
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
