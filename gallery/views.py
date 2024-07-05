from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photo, WeeklyHighlight

def gallery_view(request):
    photos = Photo.objects.all().order_by('-upload_date')
    highlights = WeeklyHighlight.objects.filter(week_start__lte=timezone.now().date()).order_by('-week_start')[:7]
    return render(request, 'gallery/gallery.html', {'photos': photos, 'highlights': highlights})

def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Photo, WeeklyHighlight
from PIL import Image
import io
from .face_recognition import process_faces

@login_required
def upload_photo(request):
    if request.method == 'POST' and request.user.is_superuser:
        image = request.FILES['image']
        img = Image.open(image)
        
        # Resize the image if it's too large
        max_size = (1920, 1080)
        img.thumbnail(max_size, Image.LANCZOS)
        
        # Save the image with optimal quality
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=85)
        output.seek(0)
        
        # Create a new InMemoryUploadedFile from the processed image
        processed_image = InMemoryUploadedFile(output, 'ImageField', f"{image.name.split('.')[0]}.jpg", 'image/jpeg', output.tell(), None)
        
        # Save the processed image to your Photo model
        photo = Photo(image=processed_image, title=request.POST['title'], description=request.POST['description'], uploader=request.user)
        photo.save()
        
        # Process faces
        process_faces(photo)
        
        return redirect('photo_detail', photo_id=photo.id)
    return render(request, 'gallery/upload.html')

def contact_admin_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('from_email')
        send_mail(subject, message, from_email, ['admin@example.com'])
        # Handle success and return appropriate feedback to the user
    return render(request, 'gallery/contact_admin_email.html')

from django.http import FileResponse
from django.shortcuts import get_object_or_404

def download_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    response = FileResponse(photo.image, as_attachment=True)
    return response