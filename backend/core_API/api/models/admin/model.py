from django.db import models
from django.core.validators import RegexValidator

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        validators=[RegexValidator(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', message="Tienes que poner un email.")],
        unique=True
    )
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)