from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from .models import *
from .forms import *


def clinics(request):
    clinics = Clinic.objects.all()
    context = {'clinics': clinics}
    return render(request, 'registry/clinics.html', context)

def clinic_add(request):
    pass
def clinic(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    vaccines = Logbook.objects.filter(clinic=clinic)
    context = {'clinic': clinic, 'vaccines': vaccines}
    return render(request, 'info/clinic.html', context)

def clinic_update(request, id):
    pass
def clinic_delete(request, id):
    pass



def doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'registry/doctors.html', context)

def doctor(request, id):
    pass
def doctor_add(request):
    pass
def doctor_update(request, id):
    pass
def doctor_delete(request, id):
    pass

def patients(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'registry/patients.html', context)

def patient(request, id):
    pass
def patient_add(request):
    pass
def patient_update(request, id):
    pass
def patient_delete(request, id):
    pass


def immunizations(request):
    immunizations = Immunization.objects.all()
    context = {'immunizations': immunizations}
    return render(request, 'registry/immunizations.html', context)

def immunization(request, id):
    pass
def immunization_add(request):
    pass
def immunization_update(request, id):
    pass
def immunization_delete(request, id):
    pass

def logbook(request):
    logbook = Logbook.objects.all()
    context = {'logbook': logbook}
    return render(request, 'registry/logbook.html', context)

def logbook_new(request):
    pass

