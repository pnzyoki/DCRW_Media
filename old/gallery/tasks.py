from celery import shared_task
from .models import WeeklyHighlight

@shared_task
def generate_weekly_highlights():
    WeeklyHighlight.generate_highlights()