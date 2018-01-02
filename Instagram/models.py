from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='add/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='Instagram/static/Instagram/images')

    def img_url(self):
        return self.photo.url[len('Instagram/images/'):]