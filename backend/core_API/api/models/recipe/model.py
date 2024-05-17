from django.db import models
from api.models.report.model import Report
from django.utils import timezone
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Report,on_delete=models.PROTECT)
    dateFinish = models.DateTimeField(default=None)
    dateCreated = models.DateTimeField(default=timezone.now, editable=False)
    active = models.BooleanField(default=True)