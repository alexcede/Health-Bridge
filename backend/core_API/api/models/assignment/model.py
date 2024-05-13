from django.db import models
from api.models.doctor.model import Doctor
from api.models.user.model import User

class Assignment(models.Model):
    id = models.AutoField(primary_key=True) 
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    dateCreated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)