from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class SignUp(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=255)
    aadhar = models.IntegerField(default=0,primary_key=True)
    dob = models.DateField()
    reg_date = models.DateTimeField(default=timezone.now, blank=True)
    user_type = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        r=str(self.rollno)
        return r


class BookAmbulance(models.Model):
    patient_name = models.CharField(max_length=50)
    accident_location_picture = models.ImageField(upload_to = 'accidents/%Y/%m/%d', blank = True)
    long = models.DecimalField(max_digits=50, decimal_places=20)
    lat = models.DecimalField(max_digits=50, decimal_places=20)
    accident_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.patient_name)
