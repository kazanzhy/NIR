from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from .models import *
from .forms import *


def clinics(request):
    pass
def clinic_add(request):
    pass
def clinic(request, id):
    pass
def clinic_update(request, id):
    pass
def clinic_delete(request, id):
    pass



def doctors(request):
    pass
def doctor(request, id):
    pass
def doctor_add(request):
    pass
def doctor_update(request, id):
    pass
def doctor_delete(request, id):
    pass

def patients(request):
    pass
def patient(request, id):
    pass
def patient_add(request):
    pass
def patient_update(request, id):
    pass
def patient_delete(request, id):
    pass


def immunizations(request):
    pass
def immunization(request, id):
    pass
def immunization_add_new(request):
    pass
def immunization_add_old(request):
    pass
def immunization_update(request, id):
    pass
def immunization_delete(request, id):
    pass

def logbook(request):
    pass
def logbook_new(request):
    pass

