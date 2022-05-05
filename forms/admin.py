from django.contrib import admin

from .models import Contact, ContactPhotos, Cake, Topper

# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactPhotos)
admin.site.register(Cake)
admin.site.register(Topper)
# admin.site.register(CakeRequestPhotos)
# admin.site.register(TopperRequestPhotos)

