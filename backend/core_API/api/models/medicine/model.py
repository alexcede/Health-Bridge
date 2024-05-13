from django.db import models
class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255, default=None)