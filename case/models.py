from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Case(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE,related_name='case_patient')
    receptionist = models.ForeignKey(User, on_delete=models.CASCADE,related_name='case_receptionist')
    description = models.CharField(max_length=500, default=None)
    filed_date = models.DateField()
    closed_date = models.DateField(default=None, null=True)
