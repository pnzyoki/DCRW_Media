from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photo/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Photo {self.id} - {self.uploaded_at}"