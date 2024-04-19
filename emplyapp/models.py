from django.db import models
from datetime import date

# Create your models here.

class Emply(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    empId=models.IntegerField(default=1000)
    # dob=models.DateField(default =date(2023, 1, 1))
    dateOfJ=models.DateField(default =date(2023, 1, 1))
    department=models.CharField(max_length=50)
    salary=models.IntegerField(default=1000)
    email=models.CharField(max_length=100, default="test@gmail.com")


    
class Leave(models.Model):
    fromDate=models.DateField(default=date(2023,1,1))
    toDate=models.DateField(default=date(2023,1,1))
    typeOfLeave=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    leaveStatus=models.CharField(max_length=100)
    user=models.CharField(max_length=255,default ='')

    
