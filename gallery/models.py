from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    faces = models.ManyToManyField('Face', blank=True)

    def __str__(self):
        return self.title

class Face(models.Model):
    name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name or f"Face {self.id}"

class WeeklyHighlight(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    week_start = models.DateField()

    @classmethod
    def generate_highlights(cls):
        current_week = timezone.now().date() - timezone.timedelta(days=timezone.now().weekday())
        photos = Photo.objects.filter(upload_date__gte=current_week)
        highlights = random.sample(list(photos), min(7, photos.count()))
        for photo in highlights:
            cls.objects.create(photo=photo, week_start=current_week)