from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Case(models.Model):
    patient = models.CharField(max_length=250)
    receptionist = models.CharField(max_length=250,)
    description = models.CharField(max_length=500, default=None)
    filed_date = models.DateField()
    closed_date = models.DateField(default=None, null=True)
