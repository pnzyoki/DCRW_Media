from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Picture
from .forms import PictureForm

def home(request):
    pictures = Picture.objects.all().order_by('-upload_date')
    return render(request, 'home.html', {'pictures': pictures})

@login_required
def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PictureForm()
    return render(request, 'upload.html', {'form': form})