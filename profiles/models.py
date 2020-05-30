

# Create your models here.
from django.db import models


class profile(models.Model):
    username = models.CharField(max_length=250),
    email = models.CharField(max_length=250),
    contact_no = models.IntegerField(),
    address = models.CharField(max_length=250),
    dob = models.DateField(),
    ONegative = 'O-'
    OPositive = 'O+'
    ANegative = 'A-'
    APositive = 'A+'
    BNegative = 'B-'
    BPositive = 'B+'
    ABNegative = 'AB-'
    ABPositive = 'AB+'
    BLOOD_CHOICES = [
        (ONegative, 'O Negative'),
        (OPositive, 'O Positive'),
        (ANegative, 'A Negative'),
        (APositive, 'A Positive'),
        (BNegative, 'B Negative'),
        (BPositive, 'B Positive'),
        (ABNegative, 'ABNegative'),
        (ABPositive, 'AB Positive')
 ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_CHOICES, default=ONegative)