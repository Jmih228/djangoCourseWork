from django.core.management import BaseCommand
from mailing import mailing_schedule


class Command(BaseCommand):

    def handle(self, *args, **options):
        mailing_schedule.main()
