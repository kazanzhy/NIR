'''
URLs for patients app
'''
from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar, name='info_calendar'),
    path('clinics/', views.clinics, name='info_clinics'),
    path('clinic/<int:id>/', views.clinic, name='info_clinic'),
    path('vaccines/', views.vaccines, name='info_vaccines'),
    path('vaccine/<int:id>/', views.vaccine, name='info_vaccine'),
]
