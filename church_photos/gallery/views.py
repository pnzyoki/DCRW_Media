# gallery/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import *
from .celery import *
from .forms import *
from twilio.rest import Client
from django.db.models.functions import TruncDate
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

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

def home_view(request):
    return render(request, 'home.html')

def send_whatsapp_message(to, message):
    client = Client('ACCOUNT_SID', 'AUTH_TOKEN')
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to}'
    )
    return message.sid

@cache_page(60 * 15)
def photo_gallery(request):
    photos = Photo.objects.all().order_by('-upload_date')
    paginator = Paginator(photos, 10)  # 10 photos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    grouped_photos = photos.annotate(upload_date_truncated=TruncDate('upload_date')).values('upload_date_truncated').distinct()
    
    return render(request, 'photo_gallery.html', {'page_obj': page_obj, 'grouped_photos': grouped_photos})

def search_photos(request):
    query = request.GET.get('q')
    filter_tag = request.GET.get('tag')
    photos = Photo.objects.all()
    
    if query:
        photos = photos.filter(description__icontains=query)
    
    if filter_tag:
        photos = photos.filter(tags__name=filter_tag)
    
    paginator = Paginator(photos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'photo_gallery.html', {'page_obj': page_obj})

def add_comment(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    if request.method == 'POST':
        comment = Comment(user=request.user, photo=photo, comment=request.POST.get('comment'))
        if request.POST.get('parent_id'):
            comment.parent_id = request.POST.get('parent_id')
        comment.save()
        send_notification_email.delay(photo.uploaded_by.email, 'New Comment on your Photo', 'Someone commented on your photo.')
    return redirect('gallery:photo_detail', photo_id=photo_id)

def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect('gallery:photo_detail', photo_id=comment.photo.id)

@login_required
def admin_dashboard(request):
    total_photos = Photo.objects.count()
    total_ratings = Rating.objects.count()
    context = {
        'total_photos': total_photos,
        'total_ratings': total_ratings,
    }
    return render(request, 'dashboard.html', context)

