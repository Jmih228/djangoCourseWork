"""
WSGI config for djangoCourseWork project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from mailing.mailing_schedule import main
from apscheduler.schedulers.background import BackgroundScheduler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCourseWork.settings')

application = get_wsgi_application()

scheduler = BackgroundScheduler()
scheduler.add_job(main, 'interval', seconds=2)
scheduler.start()
