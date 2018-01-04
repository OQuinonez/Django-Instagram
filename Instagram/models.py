from django.db import models
from django import forms


class Topics(models.Model):
    choice = models.CharField(max_length=8)

    def __str__(self):
        return self.choice


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Instagram/static/Instagram/images')
    choosing = models.ForeignKey(Topics, on_delete=models.CASCADE)

    def img_url(self):
        return self.photo.url[len('Instagram/images/'):]


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    document = models.ForeignKey(
        Document, on_delete=models.SET_NULL, blank=True, null=True)
