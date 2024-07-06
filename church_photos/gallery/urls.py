from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
]