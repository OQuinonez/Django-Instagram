from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import AddPicForm

# Create your views here.


def hello(request):
    return HttpResponse("Hello")


def add_pic(request):
    form = AddPicForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(hello(request))
    else:
        return render(request, 'Instagram/add.html', {'form': form})
