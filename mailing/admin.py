from django.contrib import admin
from mailing.models import Mail, Message


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date',
                    'send_time', 'send_frequency', 'status')
    list_filter = ('start_date', 'end_date', 'send_frequency', 'send_time')
    search_fields = ('title', 'start_date', 'end_date')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'body', 'mail')
    list_filter = ('subject', 'mail')
    search_fields = ('subject', 'body', 'mail')
