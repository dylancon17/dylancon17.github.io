from django.contrib import admin

from .models import TopperGalleryImages, TopperGalleryWriting, CakeGalleryWriting, CakeGalleryImages
# Register your models here.

admin.site.register(TopperGalleryImages)
admin.site.register(TopperGalleryWriting)
admin.site.register(CakeGalleryImages)
admin.site.register(CakeGalleryWriting)
