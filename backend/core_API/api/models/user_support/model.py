from django.db import models
from django.core.validators import RegexValidator
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
        validators=[RegexValidator(r'^\d{9,15}$', message="El número de teléfono debe tener entre 9 y 15 dígitos.")],
        unique=True,
    )
    active = models.BooleanField(default=True)