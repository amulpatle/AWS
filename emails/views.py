from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from dataentry.utils import send_email_notificaton
from django.conf import settings
# Create your views here.

def send_email(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST,request.FILES)
        if email_form.is_valid():
            email_form.save()

            # send email
            mail_subject = request.POST.get('subject')
            message = request.POST.get('body')
            to_email = settings.DEFAULT_TO_EMAIL
            send_email_notificaton(mail_subject,message,to_email)
            messages.success(request,'Email send successfully!')
            return redirect('send_email')
            
    else:
        email_form = EmailForm()
        context = {
            'email_form':email_form
        }
        return render(request,'emails/send-email.html',context)