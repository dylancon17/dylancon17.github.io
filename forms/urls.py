from django.urls import path
from . import views

urlpatterns = [
    path ('contact', views.contact, name="contact"),
    path ('cakes/request', views.cake_request, name="cake_request"),
    path ('toppers/request', views.topper_request, name="topper_request"),
]