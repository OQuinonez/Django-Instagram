from django.urls import path
from . import views

app_name = 'Instagram'

urlpatterns = [
    path('add/', views.AddPic.as_view(), name='add'),
    path('feed/', views.PicView.as_view(), name='feed'),
    path('delete/<image_id>', views.DeletePic.as_view(), name='delete')
]
