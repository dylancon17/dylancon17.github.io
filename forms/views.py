from django.shortcuts import render
from.models import Contact, ContactPhotos, Cake, Topper
from forms.forms import ContactForm, CakeForm, TopperForm
from .emails import cakes_email, toppers_email, questions_email
# from.models import None

# Create your views here.

def contact(request):
    information = ContactPhotos.objects.get(pk=1)
    form = ContactForm()
    context = {'form': form, 'information':information}

    if request.method == 'POST':
        
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        questions_email(request)
        
    return render(request, 'forms/contact.html', context)

def cake_request(request):
    # information = CakeRequestPhotos.objects.get(pk=1)
    form = CakeForm()
    context = {'form': form}

    if request.method == 'POST':
        
        Cake.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

        cakes_email(request)

    return render(request, 'forms/cake-request.html', context)

def topper_request(request):

    # information = TopperRequestPhotos.objects.get(pk=1)
    form = TopperForm()
    context = {'form': form}

    if request.method == 'POST':
        
        Topper.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

        toppers_email(request)

    return render(request, 'forms/topper-request.html', context)