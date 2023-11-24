from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'email_verificated', 'first_name',
                    'last_name', 'phone', 'country')
    list_filter = ('email', 'email_verificated', 'first_name', 'last_name', 'country')
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'country')
