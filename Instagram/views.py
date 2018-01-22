from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from .forms import AddPicForm, Filters, CommentForm
from Instagram import models
from PIL import Image, ImageFilter


def make_obj(picture):
    comments = []
    comment_set = picture.comment_set.all()
    for c in comment_set:
        comments.append(c.comment)
    return {
        'url': picture.photo.url.replace('Instagram/static', ''),
        'description': picture.description,
        'id': picture.id,
        'comments': comments
    }


class PicView(View):
    def get(self, request):
        picture_objects = models.Document.objects.all()
        pictures = []
        for picture in picture_objects:
            pictures.append(make_obj(picture))

        return render(request, 'Instagram/feed.html',
                      {'pictures': pictures,
                       'post_comment': CommentForm()})


class AddPic(View):
    def get(self, request):
        form = AddPicForm(request.POST, request.FILES)
        return render(request, 'Instagram/add.html', {'form': form})

    def post(self, request):
        form = AddPicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Instagram:feed')
        else:
            return render(request, 'Instagram/add.html', {'form': form})


class DeletePic(View):
    def post(self, request, image_id):
        models.Document.objects.get(id=image_id).delete()
        return redirect('Instagram:feed')


class AddFilter(View):
    def get(self, request, image_id):
        form = Filters()
        path = 'Instagram/static/' + models.Document.objects.get(
            id=image_id).img_url()
        return render(request, 'Instagram/feed.html', {'form': form})

    def post(self, request, image_id):
        form = Filters(request.POST)
        path = 'Instagram/static/' + models.Document.objects.get(
            id=image_id).img_url()
        image = Image.open(path)
        if form.is_valid():
            f = form.apply_filter()
            image.convert('RGB').filter(f).save(path)
            return redirect('Instagram:feed')
        return render(request, 'Instagram/filter.html', {'form': form})


class InsertComment(View):
    def post(self, request, image_id):
        pic = models.Document.objects.get(id=image_id)
        form = CommentForm(pic, request.POST)
        if form.is_valid():
            form.saveComment()
            return redirect('Instagram:feed')
        else:
            return redirect('Instagram:feed')