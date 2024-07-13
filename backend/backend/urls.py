from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gallery.views import PictureViewSet

router = DefaultRouter()
router.register(r'pictures', PictureViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)