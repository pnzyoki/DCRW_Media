from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/download/', views.download_photo, name='download_photo'),
]