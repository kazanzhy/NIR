'''
URLs for registry app
'''

from django.urls import path
from . import views

urlpatterns = [
    path('clinics/', views.clinics, name='clinics'),
    path('clinic/<int:id>', views.clinic, name='clinic'),
    path('clinic/add', views.clinics, name='clinic_add'),
    path('clinic/update', views.clinics, name='clinic_update'),
    path('clinic/delete', views.clinics, name='clinic_delete'),

    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
    path('immunizations/', views.immunizations, name='immunizations'),



    path('logbook/', views.logbook, name='logbook'),
]

