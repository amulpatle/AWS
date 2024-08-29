from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return self.customer_name
    

class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    joining_date = models.DateField(max_length=10)
    email_iD = models.EmailField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
