from django.db import models

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