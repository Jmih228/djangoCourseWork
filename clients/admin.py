from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'fullname', 'comment')
    list_filter = ('email', 'fullname', 'comment')
    search_fields = ('email', 'fullname', 'comment')
