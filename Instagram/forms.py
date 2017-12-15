from django import forms
from .models import Document


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'Document', )