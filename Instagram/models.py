from django.db import models
from django import forms

# class Topics(models.Model):
#     nature = 'Nature'
#     sports = 'Sports'
#     code = 'Code'
#     animals = 'Animals'
#     other = 'Other'
#     TOPIC_CHOICES = ((nature, 'NATURE'), (sports, 'SPORTS'), (code, 'CODE'),
#                      (animals, 'ANIMALS'), (other, 'OTHER'))
#     choice = models.CharField(choices=TOPIC_CHOICES, default='')


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Instagram/static/Instagram/images')

    def img_url(self):
        return self.photo.url[len('Instagram/images/'):]


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)