from django.apps import apps
import hashlib
import time
from django.core.management.base import CommandError
import csv
from django.db import DataError
from django.conf import settings
from django.core.mail import EmailMessage
import datetime
import os
from emails.models import Email,Sent,EmailTracking,Subscriber
from bs4 import BeautifulSoup



def get_all_custom_models():
    # Try to get all the apps
    default_models = ['ContentType','Session','LogEntry','Group','Permission','User','Upload']
    custom_models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)

    return custom_models

def check_csv_errors(file_path,model_name):
    # search for the model name across all installed apps
    model = None
        
    for app_config in apps.get_app_configs():
            # Try to search for the model
        try:
            model = apps.get_model(app_config.label,model_name)
            break
        except LookupError:
                continue #model not found in this app, contiue searching in next app.
            
    if not model:
        raise CommandError(f'Model "{model_name}" not found in any app!')
    
    # get all the field name of the model that we found
        
    model_fields = [field.name for field in model._meta.fields  if field.name  != 'id']
    try:
        with open(file_path,'r')as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames
                
            # compare csv header with model's field names
            if csv_header != model_fields:
                raise DataError(f"CSV file doesn't match with the {model_name } table fields.")
    except Exception as e:
        raise e
    
    return model
    

def send_email_notificaton(mail_subject,message,to_email,attachment=None,email_id=None):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        for recipent_email in to_email:
            # Create EmailTracking record
            if email_id:
                email = Email.objects.get(pk=email_id)
                subscriber = Subscriber.objects.get(email_list=email.email_list,email_address=recipent_email)
                timestamp = str(time.time())
                data_to_hash = f"{recipent_email}{timestamp}"
                unique_id = hashlib.sha256(data_to_hash.encode()).hexdigest()
                email_tracking = EmailTracking.objects.create(
                    email = email,
                    subscriber = subscriber,
                    unique_id = unique_id,
                )
                base_url = settings.BASE_URL
                # Generate the tracking pixel
                click_tracking_url = f"{base_url}/emails/track/click/{unique_id}"
                
                # Search for the links in the email body
                soup = BeautifulSoup(message, 'html.parser')
                urls = [a['href'] for a in soup.find_all('a', href=True)]
                print(f"Found URLs: {urls}")
                
                # If ther are links or urls in the email body, inject out click tracking url to that original link
                if urls:
                    new_message = message
                    print(urls)
                    print(new_message)
                    for url in urls:
                        # make th final tracking url
                        tracking_url = f"{click_tracking_url}?url={url}"
                        new_message = new_message.replace(f"{url}", f"{tracking_url}")
                        print(f"Tracking URL added: {tracking_url}")
                        
                else:
                    print('No URLs found in the email content')
            else:
                new_message = message
                
                # If there are links or urls in the email body, inject our click tracking url to that original link
            
            mail = EmailMessage(mail_subject,new_message,from_email,to=[recipent_email])
            if attachment is not None:
                mail.attach_file(attachment)
            mail.content_subtype = "html"
            mail.send()
        if email:
            sent = Sent()
            sent.email = email
            sent.total_sent = email.email_list.count_emails()
            sent.save()
    except Exception as e:
        raise e
    
def generate_csv_file(model_name):   
    # generate the timestampof current data and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%-M-%S")
    
    export_dir = 'exported_data'
    file_name = f'exported_{model_name}_data_{timestamp}.csv'
    file_path = os.path.join(settings.MEDIA_ROOT,export_dir,file_name)
    
    
    return file_path