from django.contrib import admin

from .models import HomePageWriting, AboutPageWriting, CakesWriting, ToppersWriting, CakesPageAdditionalImages, CakesPageInitialImages, ToppersPageAdditionalImages, ToppersPageInitialImages, CurrentToppersForSale

# Register your models here.

admin.site.register(HomePageWriting)
admin.site.register(AboutPageWriting)
admin.site.register(ToppersWriting)
admin.site.register(CakesWriting)
admin.site.register(CakesPageInitialImages)
admin.site.register(CakesPageAdditionalImages)
admin.site.register(ToppersPageInitialImages)
admin.site.register(ToppersPageAdditionalImages)
admin.site.register(CurrentToppersForSale)