from django import forms
from .models import Document

# from PIL import Image


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'photo', )


class DisplayPicForm(forms.Form):
    image = forms.ImageField()