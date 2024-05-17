from django.db import models
from api.models.doctor.model import Doctor
from api.models.user.model import User
from django.utils import timezone

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    reportName = models.CharField(max_length=255, default="Informe medico")
    disease = models.CharField(max_length=255, default=None)
    reportInfo = models.CharField(max_length=255)
    dateCreated = models.DateTimeField(default=timezone.now, editable=False)