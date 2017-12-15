from django.db import models

# from PIL import Image


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='add/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='static/images')