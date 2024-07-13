from rest_framework import viewsets
from .models import Picture
from .serializers import PictureSerializer
from rest_framework.permissions import IsAuthenticated

class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all().order_by('-upload_date')
    serializer_class = PictureSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated,]
        else:
            self.permission_classes = []
        return super().get_permissions()