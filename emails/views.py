from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from dataentry.utils import send_email_notificaton
from django.conf import settings
from .models import Subscriber
from .tasks  import send_email_task
# Create your views here.

def send_email(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST,request.FILES)
        if email_form.is_valid():
            email_form = email_form.save()

            # send email
            mail_subject = request.POST.get('subject')
            message = request.POST.get('body')
            email_list = request.POST.get('email_list')
            # Access the select email list
            email_list = email_form.email_list
             
            # Extract email addresses from the Subscriber model in the selected email list
            subscribers = Subscriber.objects.filter(email_list=email_list)
            
            to_email = [email.email_address for email in subscribers]
            if email_form.attachment:
                attachment = email_form.attachment.path
            else:
                attachment = None
            # handover email sending task to celery
            send_email_task.delay(mail_subject,message,to_email,attachment)
            messages.success(request,'Email send successfully!')
            return redirect('send_email')
            
    else:
        email_form = EmailForm()
        context = {
            'email_form':email_form
        }
        return render(request,'emails/send-email.html',context)