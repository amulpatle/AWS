import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student
import datetime
#proposed command = python3 manage.py exportdata

class Command(BaseCommand):
    help = 'Export data from student model to CSV file'
    
    def handle(self,*args,**kwargs):
        # fatch the data from the database
        student = Student.objects.all()
        
        # generate the timestampof current data and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%-M-%S")
        
        
        # define the csv file nama/path
        file_path = f'exported_student_data_{timestamp}.csv'
        print(file_path)
        
        # open the csv file and write the data
        