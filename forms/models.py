from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=400, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Page - Customer Requests"

    def __str__(self):
        return self.name

class ContactPhotos(models.Model):
    Image_Rectangle = models.ImageField(null=True, default="temp.png", help_text = "")
    Image_Circle = models.ImageField(null=True, default="temp.png", help_text = "")


    class Meta:
        verbose_name_plural = "Contact Page - Images"

    def __str__(self):
        return "Contact Page"


class Cake(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=400, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = 'Cake'

    class Meta:
        verbose_name_plural = "Cake Request Page - Customer Requests"

    def __str__(self):
        return self.name

class Topper(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=400, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = 'Topper'

    class Meta:
        verbose_name_plural = "Topper Request Page - Customer Requests"

    def __str__(self):
        return self.name

# class CakeRequestPhotos(models.Model):
#     Image_left = models.ImageField(null=True, default="temp.png", help_text = "Please note these won't show on mobile")
#     Image_right = models.ImageField(null=True, default="temp.png", help_text = "")

#     class Meta:
#         verbose_name_plural = "Cake Request Page - Images"

#     def __str__(self):
#         return "Cake Page"

# class TopperRequestPhotos(models.Model):
#     Image_left = models.ImageField(null=True, default="temp.png", help_text = "Please note these won't show on mobile")
#     Image_right = models.ImageField(null=True, default="temp.png", help_text = "")

#     class Meta:
#         verbose_name_plural = "Topper Request Page - Images"

#     def __str__(self):
#         return "Topper Page"