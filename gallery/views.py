from django.shortcuts import render

from gallery.models import TopperGalleryImages, TopperGalleryWriting, CakeGalleryImages, CakeGalleryWriting
# Create your views here.

def cakegallery(request):
    information = CakeGalleryWriting.objects.get(pk=1)
    images = CakeGalleryImages.objects.all()
    context = {'information': information, 'images':images}
    return render(request, 'gallery/gallery.html', context)

def toppergallery(request):
    information = TopperGalleryWriting.objects.get(pk=1)
    images = TopperGalleryImages.objects.all()
    context = {'information': information, 'images':images}
    return render(request, 'gallery/gallery.html', context)