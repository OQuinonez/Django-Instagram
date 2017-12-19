from django.urls import path
from . import views

app_name = 'Instagram'

urlpatterns = [
    path('add/', views.add_pic, name='add'),
    path('hello/', views.hello, name='hello'),
]
