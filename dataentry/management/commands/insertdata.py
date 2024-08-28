from django.core.management.base import BaseCommand
from dataentry.models import Student
class Command(BaseCommand):
    help = 'it will add data to database'
    
    def handle(self,*args,**kwargs):
        
        dataset = [
            {'roll_no':1002,'name':'Atul','age':25},
            {'roll_no':1003,'name':'Rohit','age':21},
            {'roll_no':1004,'name':'Sachin','age':24},
            {'roll_no':1005,'name':'Ashish','age':28},
        ]
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                
                Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING('student with roll no {roll_no} already exists'))
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))