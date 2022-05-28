from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    birth_date = models.DateField('Date Of Birth(YYYY-MM-DD)',null=True, blank=True)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,)
    height = models.FloatField('Height(in cm):',default=0)