from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_photos.settings')

app = Celery('church_photos')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# gallery/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email(user_email, subject, message):
    send_mail(subject, message, 'admin@example.com', [user_email])