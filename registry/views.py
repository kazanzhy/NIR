from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

from .models import *
from .forms import *


def clinics(request):
    if request.method == 'POST':
        form = ClinicsSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['locality'] is not None:
                clinics = Clinic.objects.filter(locality = form.cleaned_data['locality'])
            elif form.cleaned_data['district'] is not None:
                form.fields['locality'].queryset = Locality.objects.filter(district = form.cleaned_data['district'])
                clinics = Clinic.objects.filter(locality__district = form.cleaned_data['district'])
            elif form.cleaned_data['region'] is not None:
                form.fields['district'].queryset = District.objects.filter(region = form.cleaned_data['region'])
                form.fields['locality'].queryset = Locality.objects.filter(district__region = form.cleaned_data['region'])
                clinics = Clinic.objects.filter(locality__district__region = form.cleaned_data['region'])
            else:
                clinics = Clinic.objects.all()
    else:
        form = ClinicsSearchForm()
        clinics = Clinic.objects.all()
    pages = Paginator(clinics, 20)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    clinics = pages.page(current_page) 
    num_pages = pages.page_range
    context = {'clinics': clinics, 'form': form, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/clinics.html', context)


def clinic(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    doctors = Doctor.objects.filter(clinic=clinic)
    context = {'doctors': doctors, 'clinic': clinic}
    return render(request, 'registry/clinic.html', context)

def clinic_add(request):
    pass
def clinic_update(request, id):
    pass
def clinic_delete(request, id):
    pass



def doctors(request):
    doctors = Doctor.objects.all()
    pages = Paginator(doctors, 20)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    doctors = pages.page(current_page) 
    num_pages = pages.page_range
    context = {'doctors': doctors, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/doctors.html', context)

def doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    immunizations =  Immunization.objects.filter(doctor = doctor)
    context = {'doctor': doctor, 'immunizations': immunizations}
    return render(request, 'registry/doctor.html', context)

def doctor_add(request):
    pass
def doctor_update(request, id):
    pass
def doctor_delete(request, id):
    pass

def patients(request):
    patients = Patient.objects.all()
    pages = Paginator(patients, 20)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    patients = pages.page(current_page) 
    num_pages = pages.page_range
    context = {'patients': patients, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/patients.html', context)

def patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    immunizations =  Immunization.objects.filter(patient = patient)
    context = {'patient': patient, 'immunizations': immunizations}
    return render(request, 'registry/patient.html', context)

def patient_add(request):
    pass
def patient_update(request, id):
    pass
def patient_delete(request, id):
    pass


def immunizations(request):
    immunizations = Immunization.objects.all()
    pages = Paginator(immunizations, 20)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    immunizations = pages.page(current_page) 
    num_pages = pages.page_range
    context = {'immunizations': immunizations, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/immunizations.html', context)

def immunization(request, id):
    immunization = get_object_or_404(Immunization, pk=id)
    context = {'immunization': immunization}
    return render(request, 'registry/immunization.html', context)

def immunization_add_new(request):
    pass
def immunization_add_old(request):
    pass
def immunization_update(request, id):
    pass
def immunization_delete(request, id):
    pass

def logbook(request):
    logbook = Logbook.objects.all()
    pages = Paginator(logbook, 20)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    logbook = pages.page(current_page) 
    num_pages = pages.page_range
    context = {'logbook': logbook, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/logbook.html', context)

def logbook_new(request):
    pass



















