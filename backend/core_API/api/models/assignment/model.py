from django.db import models
from api.models.doctor.model import Doctor
from api.models.user.model import User
from django.utils import timezone
class Assignment(models.Model):
    id = models.AutoField(primary_key=True) 
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dateCreated = models.DateTimeField(default=timezone.now, editable=False)
    active = models.BooleanField(default=True)