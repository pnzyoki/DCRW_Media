import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photo_gallery.settings')

app = Celery('DCRW_Media')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()