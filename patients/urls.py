'''
URLs for patients app
'''
from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar),
    path('clinics/', views.clinics),
    path('clinic/<int:id>/', views.clinic),
    path('vaccines/', views.vaccines),
    path('vaccine/<int:id>/', views.vaccine),
]
