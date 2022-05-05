from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


def cakes_email(request):
    send_mail(
        subject="Cake request from " + request.POST.get('name'),
        message='Hi Jenelle!\nHere\'s a submission from your website on the Cake Request page\n\nName : ' + request.POST.get('name') + '\nEmail : ' + request.POST.get('email') + '\nPhone : ' + request.POST.get('phone') + '\nDate : ' + datetime.now().strftime("%d/%m/%Y %H:%M") +'\n\nMessage : \n' + request.POST.get('message'),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS]
    )
    return

def toppers_email(request):
    send_mail(
        subject="Topper request from " + request.POST.get('name'),
        message='Hi Jenelle!\nHere\'s a submission from your website on the Topper Request page\n\nName : ' + request.POST.get('name') + '\nEmail : ' + request.POST.get('email') + '\nPhone : ' + request.POST.get('phone') + '\nDate : ' + datetime.now().strftime("%d/%m/%Y %H:%M") +'\n\nMessage : \n' + request.POST.get('message'),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS]
    )
    return


def questions_email(request):
    send_mail(
        subject="Question from " + request.POST.get('name'),
        message='Hi Jenelle!\nHere\'s a submission from your website on the questions/contact you page\n\nName : ' + request.POST.get('name') + '\nEmail : ' + request.POST.get('email') + '\nDate : ' + datetime.now().strftime("%d/%m/%Y %H:%M") +'\n\nMessage : \n' + request.POST.get('message'),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS]
    )
    return