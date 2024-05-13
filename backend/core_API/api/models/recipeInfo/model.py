from django.db import models
from api.models.user.model import User
from api.models.doctor.model import Doctor
from api.models.report.model import Report

class RecipeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    doctorId = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    reportId = models.ForeignKey(Report, on_delete=models.PROTECT)
    dateFinish = models.DateTimeField(default=None)
    dateCreated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)