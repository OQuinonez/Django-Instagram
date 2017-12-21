from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import AddPicForm
from Instagram import models
from PIL import Image

def display_pic(request):
    pictures = [
        picture.photo.url.replace('Instagram/static', '')
        for picture in models.Document.objects.all()
    ]
    return render(request, 'Instagram/feed.html', {'pictures': pictures})


def add_pic(request):
    form = AddPicForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Instagram:feed')
    else:
        return render(request, 'Instagram/add.html', {'form': form})
