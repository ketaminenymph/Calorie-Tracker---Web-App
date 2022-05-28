import datetime

from django import forms
from django.forms import ModelForm
from .models import Event, bmiCalculate
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields=['name','event_date']
        

class bmiCalculateForm(ModelForm):
    class Meta:
        model = bmiCalculate
        fields = ['height','weight','date_rec']

    