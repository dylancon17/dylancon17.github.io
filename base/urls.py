from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name="home"),
    path ('about', views.about, name="about"),
    path ('cakes', views.cakes, name="cakes"),
    path ('toppers', views.toppers, name="toppers"),
    # path ('gallery', views.gallery, name="gallery"),
]