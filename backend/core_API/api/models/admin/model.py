from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)