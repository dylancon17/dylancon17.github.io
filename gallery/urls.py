from django.urls import path
from . import views

urlpatterns = [
    path('topper-gallery', views.toppergallery, name='toppergallery'),
    path('cake-gallery', views.cakegallery, name='cakegallery'),

]