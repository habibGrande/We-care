from django.db import models

# Create your models here.


class Feedback(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    patient = models.ForeignKey(Feedback, related_name='patient',on_delete=models.CASCADE)
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




    

