from django.urls import path
from . import views

app_name = 'Instagram'

urlpatterns = [
    path('add/', views.AddPic.as_view(), name='add'),
    path('feed/', views.PicView.as_view(), name='feed'),
    # path('choosing', views.ChoosePic.as_view(), name='choosing'),
    path('delete/<image_id>', views.DeletePic.as_view(), name='delete'),
    path('filter/<image_id>', views.AddFilter.as_view(), name='filter'),
    path('comment/<image_id>', views.InsertComment.as_view(), name='comment')
]
