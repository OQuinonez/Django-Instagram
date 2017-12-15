from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Instagram import forms
from .forms import AddPicForm

# Create your views here.


def add_pic(request):
    if request.method == 'POST':
        form = AddPicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPicForm()
    return render(request, 'Instagram/add.html', {'form': form})