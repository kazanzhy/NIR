from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('regions/', views.regions, name='api_regions'),
    path('districts/', views.districts, name='api_districts'),
    path('localities/', views.localities, name='api_localities'),
    path('clinics/', views.clinics, name='api_clinics'),
    path('doctors/', views.doctors, name='api_doctors'),
    path('patients/', views.patients, name='api_patients'),
    path('vaccines/', views.vaccines, name='api_vaccines'),
    path('diseases/', views.diseases, name='api_diseases'),
]
