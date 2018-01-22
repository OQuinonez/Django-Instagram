from django import forms
from .models import Document, Comment
from PIL import ImageFilter


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'photo', 'choosing', )


class DisplayPicForm(forms.Form):
    image = forms.ImageField()


class Filters(forms.Form):
    f_choices = [('', ''), ('BLUR', 'BLUR'), ('CONTOUR', 'CONTOUR'),
                 ('DETAIL', 'DETAIL'), ('EDGE_ENHANCE', 'EDGE_ENHANCE'),
                 ('EDGE_ENHANCE_MORE',
                  'EDGE_ENHANCE_MORE'), ('EMBOSS', 'EMBOSS'), ('FIND_EDGES',
                                                               'FIND_EDGES'),
                 ('SMOOTH', 'SMOOTH'), ('SMOOTH_MORE',
                                        'SMOOTH_MORE'), ('SHARPEN', 'SHARPEN')]
    Choose_A_Filter = forms.ChoiceField(choices=f_choices)

    def apply_filter(self):
        return {
            'BLUR': ImageFilter.BLUR,
            'CONTOUR': ImageFilter.CONTOUR,
            'DETAIL': ImageFilter.DETAIL,
            'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
            'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
            'EMBOSS': ImageFilter.EMBOSS,
            'FIND_EDGES': ImageFilter.FIND_EDGES,
            'SMOOTH': ImageFilter.SMOOTH,
            'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
            'SHARPEN': ImageFilter.SHARPEN
            # 'CUSTOM1': frozen_filter()
        }.get(self.cleaned_data['Choose_A_Filter'], None)


# class topics(forms.Form):
#     t_choices = [('', ''), ('NATURE', 'NATURE'), ('OTHER', 'OTHER'),
#                  ('ANIMALS', 'ANIMALS'), ('CODE', 'CODE'), ('SPORTS',
#                                                             'SPORTS')]

#     Choose_A_Topic = forms.ChoiceField(choices=t_choices)


class CommentForm(forms.Form):
    comment = forms.CharField()

    def __init__(self, document=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.document = document

    def saveComment(self):
        return self.document.comment_set.create(
            comment=self.cleaned_data['comment'])
