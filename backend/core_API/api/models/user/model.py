from django.db import models
from django.core.validators import RegexValidator
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        validators=[RegexValidator(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', message="Tienes que poner un email.")],
        unique=True
    )
    password = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=255)
    secondSurname = models.CharField(max_length=255)
    phoneNumber = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\d{9,15}$', message="El número de teléfono debe tener entre 9 y 15 dígitos.")],
        unique=True,
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
        validators=[RegexValidator(r'^[0-9]{8}[a-zA-Z]$', message="El DNI debe tener el formato 12345678X.")],
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