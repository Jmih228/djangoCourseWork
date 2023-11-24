from django.contrib import admin
from logs.models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_mailing_time', 'mail_status', 'mail_server_answer')
    list_filter = ('last_mailing_time', 'mail_status', 'mail_server_answer')
    search_fields = ('last_mailing_time', 'mail_status', 'mail_server_answer')
