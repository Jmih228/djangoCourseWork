from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email='manager@sky.pro',
            first_name='manager',
            last_name='manager',
            is_staff=True,
            is_superuser=False
        )

        user.set_password('hghghg777')
        user.save()
