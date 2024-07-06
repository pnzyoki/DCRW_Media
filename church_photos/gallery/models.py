from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/', processors=[ResizeToFill(800, 600)], format='PNG', options={'quality': 70})
    thumbnail = ProcessedImageField(upload_to='thumbnails/', processors=[ResizeToFill(200, 200)], format='PNG', options={'quality': 60})
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    highlight_period = models.BooleanField(default=False)
    tags = TaggableManager()
    ratings = models.ManyToManyField(User, through='Rating', related_name='photo_ratings')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
