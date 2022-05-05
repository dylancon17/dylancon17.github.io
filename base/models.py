from statistics import mode
from webbrowser import BackgroundBrowser
from django.db import models

# Create your models here.
class HomePageWriting(models.Model):
    Overall_website_description = models.TextField(null=True, max_length=400)
    home_image_main = models.ImageField(null=True, default="temp.png", help_text = "Big circular image on home page. Should be one of your best images/ nice picture of you. Light background would be best")
    
    home_image_1 = models.ImageField(null=True, default="temp.png", help_text = "Image 1/4 going underneath website description. Recommended to be cake/topper")
    home_image_2 = models.ImageField(null=True, default="temp.png", help_text = "Image 2/4 going underneath website description. Recommended to be cake/topper")
    home_image_3 = models.ImageField(null=True, default="temp.png", help_text = "Image 3/4 going underneath website description. Recommended to be cake/topper")
    home_image_4 = models.ImageField(null=True, default="temp.png", help_text = "Image 4/4 going underneath website description. Recommended to be cake/topper")

    Cakes_Title = models.CharField(max_length=50, null=True)
    cakes_image = models.ImageField(null=True, default="temp.png", help_text = "Image going with cakes popup. Recommended to be a cake")
    Cakes_More_Info = models.TextField(null=True, max_length=200, help_text = "The text has to take up 7 lines (when viewing on computer) on the page for proper formatting")

    Toppers_Title = models.CharField(max_length=50, null=True)
    toppers_image = models.ImageField(null=True, default="temp.png", help_text = "Image going with toppers popup. Recommended to be a topper")
    Toppers_More_Info = models.TextField(null=True, max_length=300, help_text = "The text has to take up 7 lines (when viewing on computer) on the page for proper formatting")

    class Meta:
        verbose_name_plural = "Home Page - Text and Images"

    def __str__(self):
        return "Home Page"

class AboutPageWriting(models.Model):
    About_Title = models.CharField(max_length=50, null=True)
    About_Description = models.TextField(null=True, max_length=400)

    Point_1_Title = models.CharField(max_length=50, null=True)
    Point_1_Description = models.TextField(null=True, max_length=400)
    Point_1_Image = models.ImageField(null=True, default="temp.png", help_text = "Will be cropped into a circle. Recommended to be relevant to your point")

    Point_2_Title = models.CharField(max_length=50, null=True)
    Point_2_Description = models.TextField(null=True, max_length=400)
    Point_2_Image = models.ImageField(null=True, default="temp.png", help_text = "Will be cropped into a circle. Recommended to be relevant to your point")

    Point_3_Title = models.CharField(max_length=50, null=True)
    Point_3_Description = models.TextField(null=True, max_length=400)
    Point_3_Image = models.ImageField(null=True, default="temp.png", help_text = "Will be cropped into a circle. Recommended to be relevant to your point. Let me know if you need less/more points overall")

    class Meta:
        verbose_name_plural = "About Page - Text and Images Upper Half"

    def __str__(self):
        return "About Page"

class CakesWriting(models.Model):
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True, max_length=400)
    Button_link = '{% url "about" %}'


    Button = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Cakes Page - Text"

    def __str__(self):
        return "Cakes Page"

class ToppersWriting(models.Model):
    Title = models.CharField(max_length=50, null=True)
    Description = models.TextField(null=True, max_length=400)

    Button = models.CharField(max_length=50, null=True)
    Button_link = '{% url "about" %}'

    Current_Designs_Title = models.CharField(max_length=50, null=True)
    Current_Designs_Description = models.TextField(null=True, max_length=400)

    class Meta:
        verbose_name_plural = "Toppers Page - Text"

    def __str__(self):
        return "Toppers Page"


class CakesPageInitialImages(models.Model):
    Image1 = models.ImageField(null=True, default="temp.png", help_text = "")
    Image2 = models.ImageField(null=True, default="temp.png", help_text = "")
    Image3 = models.ImageField(null=True, default="temp.png", help_text = "")

    class Meta:
        verbose_name_plural = "Cakes Page - Images"

    def __str__(self):
        return "Initial Page"

class CakesPageAdditionalImages(models.Model):
    Image_left = models.ImageField(null=True, default="temp.png", help_text = "")
    Image_centre = models.ImageField(null=True, default="temp.png", help_text = "")
    Image_right = models.ImageField(null=True, default="temp.png", help_text = "")

    class Meta:
        verbose_name_plural = "Cakes Page - Images Optional"

    def __str__(self):
        return "Additional Pages"

class ToppersPageInitialImages(models.Model):
    Image1 = models.ImageField(null=True, default="temp.png", help_text = "")
    Image2 = models.ImageField(null=True, default="temp.png", help_text = "")
    Image3 = models.ImageField(null=True, default="temp.png", help_text = "")

    class Meta:
        verbose_name_plural = "Toppers Page - Images"

    def __str__(self):
        return "Initial Page"

class ToppersPageAdditionalImages(models.Model):
    Image_left = models.ImageField(null=True, default="temp.png", help_text = "")
    Image_centre = models.ImageField(null=True, default="temp.png", help_text = "")
    Image_right = models.ImageField(null=True, default="temp.png", help_text = "")

    class Meta:
        verbose_name_plural = "Toppers Page - Images Optional"

    def __str__(self):
        return "Additional Pages"

class CurrentToppersForSale(models.Model):
    Name = models.CharField(max_length=50, null=True)
    Cost = models.TextField(null=True, max_length=400, help_text="Numbers only please with two decimals! ex 13.95")
    Image = models.ImageField(null=True, default="temp.png")
    Url = models.URLField(null=True, max_length=400)

    class Meta:
        verbose_name_plural = "Toppers Page - Current Postings"

    def __str__(self):
        return self.Name