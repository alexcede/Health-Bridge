from django.db import models

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