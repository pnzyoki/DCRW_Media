from django.urls import path
from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', home_view, name='home'),
    path('upload/', upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),
]