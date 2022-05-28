import datetime

from django.shortcuts import render, get_object_or_404
from main.models import Event, bmiCalculate
from django.http import HttpResponse
from django.urls import reverse

from .forms import EventForm, bmiCalculateForm

def dashboard(request):
    return render(request, 'main/dashboard.html')

'''def testwrite(request):
    return render(request, 'main/testwrite.html')'''

def testwrite(request):
    if request.method =='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            events = Event.objects.all()
            return render(request,'main/testwrite2.html', {'events':events,})

    else:
        form = EventForm()
        

    return render(request, 'main/testwrite.html', {'form': form})


def testbmi(request):
    if request.method=="POST":
        form = bmiCalculateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.bmi = request.user
            obj.username = request.user.username
            obj.save()
            #bmi = bmiCalculate.objects.all()
            bmi = bmiCalculate.objects.filter(username=request.user.username)
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            bmi_init = round(((weight/height**2)*10000),2)
            #u.bmi = bmi_init

            return render(request,'main/testbmi2.html', {'bmi':bmi,'bmi_init':bmi_init})

    else:
        form = bmiCalculateForm()
    

    return render(request, 'main/testbmi.html', {'form': form})