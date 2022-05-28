import datetime

from django.db import models
from django.forms import ModelForm

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')

     def __str__(self):
        return self.name

class bmiCalculate(models.Model):
    height = models.FloatField('Height(in cm):')
    weight = models.FloatField('Weight(in kg):')
    date_rec = models.DateField('Date:', default=datetime.datetime.now)
    bmi = models.FloatField()
    username = models.CharField(max_length=200,default='SOME STRING')

    def __str__(self):
        return self.name

    def bmi(self):
        return round((self.weight/self.height**2)*10000,2)
