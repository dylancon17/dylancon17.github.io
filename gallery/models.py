from django.db import models

# Create your models here.
class TopperGalleryImages(models.Model):
    Image = models.ImageField(null=True, default="temp.png", help_text = "Please add as many as you would like!")

    class Meta:
        verbose_name_plural = "Topper Gallery Page - Images"

    def __str__(self):
        return "Image"

class CakeGalleryImages(models.Model):
    Image = models.ImageField(null=True, default="temp.png", help_text = "Please add as many as you would like!")

    class Meta:
        verbose_name_plural = "Cake Gallery Page - Images"

    def __str__(self):
        return "Image"

class TopperGalleryWriting(models.Model):
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True, max_length=400)

    class Meta:
        verbose_name_plural = "Topper Gallery Page - Text"

    def __str__(self):
        return "Topper Gallery"
        
class CakeGalleryWriting(models.Model):
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True, max_length=400)

    class Meta:
        verbose_name_plural = "Cake Gallery Page - Text"

    def __str__(self):
        return "Cake Gallery"

