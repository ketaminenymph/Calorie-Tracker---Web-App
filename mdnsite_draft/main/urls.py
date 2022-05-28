from django.urls import path
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