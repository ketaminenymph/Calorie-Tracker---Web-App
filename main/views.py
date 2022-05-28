import datetime
from datetime import date
from random import randint

from django.shortcuts import render, get_object_or_404, render_to_response
from main.models import Event, bmiCalculate, bmrCalculate, calorieLog
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.urls import reverse

from .forms import EventForm, bmiCalculateForm, bmrCalculateForm, calorieLogForm
from accounts.models import User


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
            obj.height = request.user.height
            obj.save()
            #bmi = bmiCalculate.objects.all()
            #bmi = bmiCalculate.objects.filter(username=request.user.username)
            bmi = bmiCalculate.objects.filter(username=request.user.username).order_by('-date_rec')
            #unsorted_results = qs.all()
            #sorted_results = sorted
            weight = form.cleaned_data['weight']
            #height = form.cleaned_data['height']
            height = request.user.height
            bmi_init = round(((weight/height**2)*10000),2)
            #obj.bmi = bmi_init

            return render(request,'main/testbmi2.html', {'bmi':bmi,'bmi_init':bmi_init})

    else:
        form = bmiCalculateForm()
    

    return render(request, 'main/testbmi.html', {'form': form})


def viewbmi(request):
    bmi = bmiCalculate.objects.filter(username=request.user.username).order_by('-date_rec')
    return render(request,'main/testbmi2.html',{'bmi':bmi})

def chartweight(request):
    dataset = bmiCalculate.objects.filter(username=request.user.username).order_by('-date_rec')[:7]
    return render(request, 'main/chartweight.html',{'dataset':dataset})

def chartcalorieintake(request):
    dataset = calorieLog.objects.filter(username=request.user.username).order_by('-date_rec')[:7]
    return render(request, 'main/chartcalorieintake.html',{'dataset':dataset})

def chartcalorieintake_vs_burnt(request):
    dataset1 = calorieLog.objects.filter(username=request.user.username).order_by('-date_rec')[:7]
    dataset2 = bmrCalculate.objects.filter(username=request.user.username).order_by('-date_rec')[:7]
    return render(request, 'main/chartcalorieintakevsburnt.html',{'dataset1':dataset1,'dataset2':dataset2})
    


def testbmr(request):
    if request.method=="POST":
        form = bmrCalculateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.bmr = request.user
            obj.username = request.user.username
            obj.sex = request.user.sex
            obj.height = request.user.height
            #obj.age = (date.today()-timedelta(request.user.birth_date))
            obj.age = (date.today().year - request.user.birth_date.year)
            obj.save()
            bmr = bmrCalculate.objects.filter(username=request.user.username).order_by('-date_rec')

            weight = form.cleaned_data['weight']
            #height = form.cleaned_data['height']
            height = request.user.height
            age = obj.age
            sex = request.user.sex
            if sex == "M":
                bmr_init = round(66.5 + (13.75 * weight) + (5 * height) - (6.755 * age))
            elif sex == "F":
                bmr_init = round(655.1 + (9.6 * weight) + (1.8*height) - (4.7 * age))
            #bmr_init = round(weight*3)
            physicalcalories_burnt_init = form.cleaned_data['physicalcalories_burnt']
            totalcalories_burnt_init = physicalcalories_burnt_init + bmr_init
            #totalcalories_burnt_init = request.bmrcalculate.totalcalories_burnt

            return render(request,'main/testbmr2.html',{'bmr':bmr,'bmr_init':bmr_init,'totalcalories_burnt_init':totalcalories_burnt_init})

    else:
        form = bmrCalculateForm()

    return render(request, 'main/testbmr.html',{'form': form})


def viewbmr(request):
    bmr = bmrCalculate.objects.filter(username=request.user.username).order_by('-date_rec')
    return render(request,'main/testbmr2.html',{'bmr':bmr})


def viewprofile(request):
    profile = User.objects.filter(username=request.user.username)
    return render(request,'main/profile.html',{'profile':profile})


def testCalorie(request):
    if request.method=="POST":
        form = calorieLogForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = request.user.username
            obj.save()
            calorie = calorieLog.objects.filter(username=request.user.username).order_by('-date_rec')

            return render(request, 'main/testcalorie2.html',{'calorie':calorie})

    else:
        form = calorieLogForm()

    return render(request, 'main/testcalorie.html',{'form':form})

def viewCalorie(request):
    calorie = calorieLog.objects.filter(username=request.user.username).order_by('-date_rec')
    return render(request,'main/testcalorie2.html',{'calorie':calorie})


