from django.forms import ModelForm
from .models import Contact, Topper, Cake

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class CakeForm(ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'email', 'phone','message']

class TopperForm(ModelForm):
    class Meta:
        model = Topper
        fields = ['name', 'email', 'phone','message']