'''

'''

from django.urls import path
from registry import views

urlpatterns = [
    path('immunizations/', views.immunizations, name='immunizations'),
    path('patients/', views.patients, name='patients'),
    path('doctors/', views.doctors, name='doctors'),
    path('clinics/', views.clinics, name='clinics'),
    path('logbook/', views.logbook, name='logbook'),
]

