import datetime
from datetime import date

from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')

     def __str__(self):
        return self.name

def clean_date(value):
    days = datetime.date.today() - value
    if value > datetime.date.today():
        raise forms.ValidationError("Invalid Date - Date in the future") 
    elif (days.days > 7):
        raise forms.ValidationError("Invalid Date - Back dates more than a week")
    return value

class bmiCalculate(models.Model):
    height = models.FloatField('Height(in cm):',default=0)
    weight = models.FloatField('Weight(in kg):',default=0)
    date_rec = models.DateField('Date(YYYY-MM-DD):', default=datetime.datetime.now,validators=[clean_date])
    #bmi = models.FloatField('BMI:',default=0)
    calculated_bmi = models.FloatField(default=0.0)
    username = models.CharField(max_length=200,default='SOME STRING')

    def __str__(self):
        return self.username

    def bmi(self):
        return round((self.weight/self.height**2)*10000,2)

    def save(self, *args, **kwargs):
        try:
            self.calculated_bmi = round(((self.weight/self.height**2)*10000),2)
        except TypeError:
            pass
        
        super(bmiCalculate,self).save(*args, **kwargs)


class bmrCalculate(models.Model):
    height = models.FloatField('Height(in cm):',default=0)
    weight = models.FloatField('Weight(in kg):',default=0)
    date_rec = models.DateField('Date(YYYY-MM-DD):',default=datetime.datetime.now,validators=[clean_date])
    calculated_bmr = models.FloatField(default=0.0)
    username = models.CharField(max_length=200,default='SOME STRING')
    age = models.FloatField(default=18.0)
    sex = models.CharField(max_length=60,default='M')
    physicalcalories_burnt = models.FloatField('Calories Burnt (kcal): ',default=0.0)
    totalcalories_burnt = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            if self.sex == "M":
                #self.calculated_bmr = round(self.weight*3)
                self.calculated_bmr = round(66.5 + (13.75 * self.weight) + (5 * self.height) - (6.755 * self.age))
            elif self.sex == "F":
                #self.calculated_bmr = round(self.weight*6)
                #self.calculated_bmr = round(655.1 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * 47))
                self.calculated_bmr = round(655.1 + (9.6 * self.weight) + (1.8*self.height) - (4.7 * self.age))
        except TypeError:
            pass

        try:
            self.totalcalories_burnt = self.physicalcalories_burnt + self.calculated_bmr
        except TypeError:
            pass

        super(bmrCalculate,self).save(*args, **kwargs)


class calorieLog(models.Model):
    calorie_intake = models.FloatField('Intake(in kcal): ',default=0)
    date_rec = models.DateField('Date(YYYY-MM-DD):',default=datetime.datetime.now,validators=[clean_date])
    username = models.CharField(max_length=200,default='SOME STRING')