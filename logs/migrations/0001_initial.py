# Generated by Django 4.2.7 on 2023-11-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_mailing_time', models.DateTimeField(verbose_name='Дата последней рассылки')),
                ('mail_status', models.CharField(max_length=50, verbose_name='Статус попытки')),
                ('mail_server_answer', models.CharField(max_length=150, verbose_name='Ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
