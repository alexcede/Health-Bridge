from django.db import models
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=255)
    dni = models.CharField(
        max_length=12,
        unique=True
    )
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=255)
    secondSurname = models.CharField(max_length=255)
    phoneNumber = models.CharField(
        max_length=20,  # Longitud máxima del número de teléfono
        unique=True
    )
    active = models.BooleanField(default=True)
    
    def completeName(self):
        completeName = "{0} {1}, {2}"
        return completeName.format(self.firstSurname, self.secondSurname, self.name)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=255)
    secondSurname = models.CharField(max_length=255)
    phoneNumber = models.CharField(
        max_length=20,  # Longitud máxima del número de teléfono
        unique=True
    )
    healthCardCode = models.CharField(
        max_length=255,
        unique=True
    )
    birthDate = models.DateField()
    genders = [
        ('F','female'),
        ('M','male')
    ]
    gender = models.CharField(
        max_length=1,
        choices=genders
    )
    dni = models.CharField(
        max_length=12,
        unique=True
    )
    address = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def completeName(self):
        completeName = "{0} {1} {2}"
        return completeName.format(self.firstSurname, self.secondSurname, self.name)
    def __str__(self):
        txt = "{0}"
        formatedDate = self.birthDate.strftime("%A %D/%m/%Y")
        return txt.format(formatedDate)

class UserSupport(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=255)
    secondSurname = models.CharField(max_length=255)
    phoneNumber = models.CharField(
        max_length=20, 
        unique=True
    )
    active = models.BooleanField(default=True)

class Assignment(models.Model):
    id = models.AutoField(primary_key=True) 
    doctorId = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    dateCreated = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    doctorId = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    reportInfo = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(auto_now_add=True)
    
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    doctorId = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    reportId = models.ForeignKey(Report, on_delete=models.PROTECT)
    medicine = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(auto_now_add=True)
