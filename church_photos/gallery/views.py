# gallery/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Photo, Rating
from .utils import recognize_faces
from .forms import PhotoForm, RatingForm
from twilio.rest import Client

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            recognize_faces(photo.image.path)
            return redirect('gallery:home')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

def photo_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.photo = photo
            rating.save()
    else:
        form = RatingForm()
    return render(request, 'photo_detail.html', {'photo': photo, 'form': form})

def home(request):
    return render(request, 'home.html')

def send_whatsapp_message(to, message):
    client = Client('ACCOUNT_SID', 'AUTH_TOKEN')
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to}'
    )
    return message.sid

@login_required
def admin_dashboard(request):
    total_photos = Photo.objects.count()
    total_ratings = Rating.objects.count()
    context = {
        'total_photos': total_photos,
        'total_ratings': total_ratings,
    }
    return render(request, 'dashboard.html', context)