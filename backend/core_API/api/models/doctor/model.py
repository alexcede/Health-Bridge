from django.db import models
from django.core.validators import RegexValidator

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        validators=[RegexValidator(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', message="Tienes que poner un email.")],
        unique=True
    )
    password = models.CharField(max_length=255)
    dni = models.CharField(
        max_length=9,
        validators=[RegexValidator(r'^[0-9]{8}[a-zA-Z]$', message="El DNI debe tener el formato 12345678X.")],
        unique=True,
    )
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=255)
    secondSurname = models.CharField(max_length=255)
    phoneNumber = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\d{9,15}$', message="El número de teléfono debe tener entre 9 y 15 dígitos.")],
        unique=True,
    )
    active = models.BooleanField(default=True)
    
    def completeName(self):
        completeName = "{0} {1}, {2}"
        return completeName.format(self.firstSurname, self.secondSurname, self.name)