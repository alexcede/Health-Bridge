from django.db import models
from api.models.doctor_model import Doctor
from api.models.user_model import User

class Assignment(models.Model):
    id = models.AutoField(primary_key=True) 
    doctorId = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    dateCreated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)