from django.db import models
from djangoCourseWork import settings


class Client(models.Model):

    email = models.EmailField(unique=True, verbose_name='email')
    fullname = models.CharField(max_length=255, verbose_name='клиент')
    comment = models.TextField(verbose_name='комментарий')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                             verbose_name='пользователь')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
