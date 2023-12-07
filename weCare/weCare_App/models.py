from django.db import models
import re
# Create your models here.
class PatientManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if(len(postData['first_name']) < 2):
            errors['first_name'] = "First Name should be at least 2 characters!"
        if(len(postData['last_name']) < 2):
            errors['last_name'] = "Last Name should be at least 2 characters!"
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confrim_password']:
            errors['con-password'] = "Passwords should be matched"
        if(len(postData['phone_number']) < 10):
            errors['phone_number'] = "Phone Number should be at least 10 digits"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):     
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        return errors



class Patient(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PatientManager()

class Feedback(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    date = models.DateField()
    patient = models.ForeignKey(Patient, related_name='feedback',on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Speciality(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Doctor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=50)
    appointments = models.ManyToManyField(Patient, through='Appointment')
    title = models.CharField(max_length=255)
    speciality = models.ForeignKey(Speciality,related_name="doctor", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointment(models.Model):
    date = models.DateField()
    Time = models.TimeField()
    doctor = models.ForeignKey(Doctor,related_name='appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,related_name='Patientppointment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    street = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=45)
    doctor = models.ManyToManyField(Doctor,related_name='hospital')
    location = models.ForeignKey(Location,related_name='hospital',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    

