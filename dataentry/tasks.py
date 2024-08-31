from awd_main.celery import app
import time
from django.core.management import call_command
from .utils import send_email_notificaton
from django.conf import settings
from .utils import generate_csv_file
@app.task
def celery_test_task():
    time.sleep(10)
    mail_subject = 'test subject'
    message = 'this is test email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notificaton(mail_subject,message,to_email)
    
    return ' Task exxecuted successfully'

@app.task
def import_data_task(file_path,model_name):
    try:
        call_command('importdata',file_path, model_name)
        
    except Exception as e:
        raise e
    #notify the user using sending email
    mail_subject = 'Import Data completed'
    message = 'Your data import has been successful'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notificaton(mail_subject,message,to_email)
    
    return 'Data imported successfully.'

@app.task
def export_data_task(model_name):   
    try:
        call_command('exportdata',model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    
    # Send email with attachment
    mail_subject = 'Export Data Successful'
    message = 'Export data successful. Please find the attachment'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notificaton(mail_subject,message,to_email,attachment=file_path)
    return 'Export Data task executed successfully'