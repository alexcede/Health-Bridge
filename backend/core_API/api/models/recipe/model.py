from django.db import models
from api.models.report.model import Report

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Report,on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    dateFinish = models.DateTimeField(default=None)
    dateCreated = models.DateTimeField(auto_now_add=True)