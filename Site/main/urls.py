from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]

urlpatterns+=[
    path('testwrite/', views.testwrite, name='testwrite'),
]

urlpatterns+=[
    path('testbmi/', views.testbmi, name='testbmi'),
]

urlpatterns+=[
    path('viewbmi/', views.viewbmi, name='viewbmi'),
]

urlpatterns+=[
    path('testbmr/', views.testbmr, name='testbmr'),
    path('viewbmr/', views.viewbmr, name='viewbmr')
]

urlpatterns+=[
    path('viewprofile/', views.viewprofile, name='viewprofile'),
]

urlpatterns+=[
    path('testcalorie/', views.testCalorie, name='testcalorie'),
    path('viewcalorie/', views.viewCalorie, name='viewcalorie'),
]

urlpatterns+=[
    path('chartweight/data', views.chartweight, name='chartweight'),
    path('chartcalorieintake/data', views.chartcalorieintake, name='chartcalorieintake'),
    path('chartcalorieintakevsburnt/data', views.chartcalorieintake_vs_burnt, name='chartcalorieintakevsburnt')
]