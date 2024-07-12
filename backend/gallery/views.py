from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *

class PhotViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        image = request.FILES.getlist('images')
        description = request.data.getlist('description')
        photos = []

        for i, image in enumerate(image):
            description =description[i] if description else ""
            photo = Photo(image=image, description=description)
            photo.save()
            photos.append(photo)
        
        serializer  = self.get_serializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)