from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import AddPicForm
from .models import Document

# Create your views here.


def hello(request):
    return HttpResponse("Hello")


def display_pic(request):
    picture = [
        picture.photo.url.replace('Instagram/static', '')
        for picture in models.Document.objects.all()
    ]


def add_pic(request):
    form = AddPicForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(display_pic(request))
    else:
        return render(request, 'Instagram/add.html', {'form': form})
