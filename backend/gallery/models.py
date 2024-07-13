from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    image = models.ImageField(upload_to='pictures/')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Picture {self.id} uploaded by {self.uploaded_by.username}"
