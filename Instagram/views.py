from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import AddPicForm
from Instagram import models
import os.path
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw


def custom_image(request):
    # The text we want to draw on the image, in this case the local time, e.g. "20:55:11":
    text = datetime.now().strftime('%H:%M:%S')

    # Specifying our background image (in this case a 200 x 75 pixels PNG image):
    base_image = os.path.join(settings.BASE_DIR,
                              'static/app_name/images/base_image.png')

    # Specifying the font file:
    font_file = os.path.join(settings.BASE_DIR,
                             'static/app_name/fonts/font_file.ttf')

    # Font color (black specified as RGB) and size:
    font_color = (0, 0, 0)
    font_size = 36

    image = Image.open(base_image)
    font = ImageFont.truetype(font_file, font_size)
    draw = ImageDraw.Draw(image)

    # Drawing the text 34 pixels from the left edge and 18 pixels from the top:
    draw.text((34, 18), text, font=font, fill=font_color)

    # Saving the image to the Django response object:
    response = HttpResponse(content_type='image/png')
    image.save(response, 'PNG')

    return response


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
