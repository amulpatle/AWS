from django.apps import apps
from django.core.management.base import CommandError
import csv
from django.db import DataError

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
    