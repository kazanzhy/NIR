from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden

import qrcode
import base64
import io

from .models import *
from .forms import *


def clinics(request):
    # Search block
    form = ClinicsSearchForm(request.GET)
    if form.is_valid():
        locality = form.cleaned_data['locality']
        district = form.cleaned_data['district']
        region = form.cleaned_data['region']
        if locality is not None:
            clinics = Clinic.objects.filter(locality = locality)
        elif district is not None:
            clinics = Clinic.objects.filter(locality__district = district)
        elif region is not None:
            clinics = Clinic.objects.filter(locality__district__region = region)
        else:
            clinics = Clinic.objects.all()
    else:
        clinics = Clinic.objects.all()
    # Pagination block
    pages = Paginator(clinics, 30)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    clinics = pages.page(current_page) 
    num_pages = pages.page_range
    # Context
    context = {'clinics': clinics, 'form': form, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/clinics.html', context)


def clinic(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    doctors = Doctor.objects.filter(clinic=clinic)
    context = {'doctors': doctors, 'clinic': clinic}
    return render(request, 'registry/clinic.html', context)


def clinic_add(request):
    if request.method == 'POST':
        form = ClinicAddForm(request.POST)
        if form.is_valid():
            clinic = Clinic()
            clinic.locality = form.cleaned_data['locality']
            clinic.clinic = form.cleaned_data['clinic']
            clinic.logo = form.cleaned_data['logo']
            clinic.info = form.cleaned_data['info']
            clinic.save()
            return redirect(reverse('clinic', args=[clinic.pk]))
    else:
        form = ClinicAddForm()
    context = {'form': form}
    return render(request, 'registry/clinic_add.html', context)


def clinic_update(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    if request.method == 'POST':
        form = ClinicAddForm(request.POST)
        if form.is_valid():
            clinic.locality = form.cleaned_data['locality']
            clinic.clinic = form.cleaned_data['clinic']
            clinic.logo = form.cleaned_data['logo']
            clinic.info = form.cleaned_data['info']
            clinic.save()
            return redirect(reverse('clinic', args=[id]))
    else:
        initial = {'locality': clinic.locality, 'clinic': clinic.clinic, 'logo': clinic.logo, 'info': clinic.info}
        form = ClinicAddForm(initial = initial)
    context = {'form': form}
    return render(request, 'registry/clinic_add.html', context)

def clinic_delete(request, id):
    return HttpResponseForbidden()


def doctors(request):
    doctors = Doctor.objects.all()
    pages = Paginator(doctors, 30)
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


def doctor_add(request, id):
    if request.method == 'POST':
        form = DoctorAddForm(request.POST)
        if form.is_valid():
            clinic = form.cleaned_data['clinic']
            last = Lastname.objects.get_or_create(lastname = form.cleaned_data['lastname'])[0]
            first = Firstname.objects.get_or_create(firstname = form.cleaned_data['firstname'])[0]
            patro = Patronymic.objects.get_or_create(patronymic = form.cleaned_data['patronymic'])[0]
            doctor, created = Doctor.objects.get_or_create(clinic=clinic, lastname=last, firstname=first, patronymic=patro)
            return redirect(reverse('doctor', args=[doctor.pk]))
    else:
        form = DoctorAddForm()
        form.fields['clinic'].queryset = Clinic.objects.filter(pk=id)
    context = {'form': form}
    return render(request, 'registry/doctor_add.html', context)


def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method == 'POST':
        form = DoctorAddForm(request.POST)
        if form.is_valid():
            doctor.clinic = form.cleaned_data['clinic']
            doctor.lastname = Lastname.objects.get_or_create(lastname = form.cleaned_data['lastname'])[0]
            doctor.firstname = Firstname.objects.get_or_create(firstname = form.cleaned_data['firstname'])[0]
            doctor.patronymic = Patronymic.objects.get_or_create(patronymic = form.cleaned_data['patronymic'])[0]
            doctor.save()
            return redirect(reverse('doctor', args=[doctor.pk]))
    else:
        initial = {'clinic':doctor.clinic, 'lastname':doctor.lastname, 'firstname':doctor.firstname, 'patronymic':doctor.patronymic}
        form = DoctorAddForm(initial = initial)
    context = {'form': form}
    return render(request, 'registry/doctor_add.html', context)

def doctor_delete(request, id):
    return HttpResponseForbidden()


def patients(request):
    form = PatientsSearchForm()
    patients = Patient.objects.all()
    pages = Paginator(patients, 30)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    if current_page not in pages.page_range:
        current_page = 1
    patients = pages.page(current_page) 
    num_pages = pages.page_range
    context = {'patients': patients, 'form': form, 'num_pages': num_pages, 'current_page': current_page}
    return render(request, 'registry/patients.html', context)


def patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    immunizations =  Immunization.objects.filter(patient = patient)
    context = {'patient': patient, 'immunizations': immunizations}
    return render(request, 'registry/patient.html', context)


def patient_add(request):
    if request.method == 'POST':
        form = PatientAddForm(request.POST)
        if form.is_valid():
            patient = Patient()
            patient.lastname = Lastname.objects.get_or_create(lastname = form.cleaned_data['lastname'])[0]
            patient.firstname = Firstname.objects.get_or_create(firstname = form.cleaned_data['firstname'])[0]
            patient.patronymic = Patronymic.objects.get_or_create(patronymic = form.cleaned_data['patronymic'])[0]
            patient.sex = form.cleaned_data['sex']
            patient.birth = form.cleaned_data['birth']
            patient.phone = form.cleaned_data['phone']
            patient.save()
            return redirect(reverse('patient', args=[patient.pk]))
    else:
        form = PatientAddForm()
    context = {'form': form}
    return render(request, 'registry/patient_add.html', context)


def patient_update(request, id):
    patient = get_object_or_404(Patient, pk=id)
    if request.method == 'POST':
        form = PatientAddForm(request.POST)
        if form.is_valid():
            patient.lastname = Lastname.objects.get_or_create(lastname = form.cleaned_data['lastname'])[0]
            patient.firstname = Firstname.objects.get_or_create(firstname = form.cleaned_data['firstname'])[0]
            patient.patronymic = Patronymic.objects.get_or_create(patronymic = form.cleaned_data['patronymic'])[0]
            patient.sex = form.cleaned_data['sex']
            patient.birth = form.cleaned_data['birth']
            patient.phone = form.cleaned_data['phone']
            patient.save()
            return redirect(reverse('patient', args=[patient.pk]))
    else:
        initial = {'lastname':patient.lastname, 'firstname':patient.firstname, 'patronymic':patient.patronymic, 
                    'sex':patient.sex, 'birth':patient.birth, 'phone':patient.phone}
        form = PatientAddForm(initial = initial)
    context = {'form': form}
    return render(request, 'registry/patient_add.html', context)


def patient_delete(request, id):
    return HttpResponseForbidden()

def patient_print(request, id):
    qr = qrcode.make(request.get_host() + request.path)
    buff = io.BytesIO()
    qr.save(buff, 'PNG')
    qrb64 = base64.b64encode(buff.getvalue()).decode('utf-8') 
    patient = get_object_or_404(Patient, pk=id)
    immunizations =  Immunization.objects.filter(patient = patient)
    context = {'patient': patient, 'immunizations': immunizations, 'qr': qrb64}
    return render(request, 'registry/patient_certificate.html', context)

def immunizations(request):
    immunizations = Immunization.objects.all()
    pages = Paginator(immunizations, 30)
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

def immunization_add(request, id):
    if request.method == 'POST':
        form = ImmunizationAddForm(request.POST)
        if form.is_valid():
            immunization = Immunization()
            immunization.clinic = form.cleaned_data['clinic']
            immunization.doctor = form.cleaned_data['doctor']
            immunization.series = form.cleaned_data['series']
            immunization.patient = form.cleaned_data['patient']
            immunization.general_reaction = form.cleaned_data['general_reaction']
            immunization.local_reaction = form.cleaned_data['local_reaction']
            immunization.contraindications = form.cleaned_data['contraindications']
            immunization.dose = form.cleaned_data['dose']
            immunization.date = form.cleaned_data['date']
            immunization.save()
            return redirect(reverse('immunization', args=[immunization.pk]))
    else:
        form = ImmunizationAddForm()
        form.fields['patient'].queryset = Patient.objects.filter(pk=id)
    context = {'form': form}
    return render(request, 'registry/immunization_add.html', context)

def immunization_update(request, id):
    pass
def immunization_delete(request, id):
    return HttpResponseForbidden()

def immunization_print(request, id):
    immunization = get_object_or_404(Immunization, pk=id)
    qr = qrcode.make(request.get_host() + request.path)
    buff = io.BytesIO()
    qr.save(buff, 'PNG')
    qrb64 = base64.b64encode(buff.getvalue()).decode("utf-8") 
    context = {'immunization': immunization, 'qr': qrb64}
    return render(request, 'registry/immunization_certificate.html', context)

def logbook(request):
    logbook = Logbook.objects.all()
    pages = Paginator(logbook, 30)
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


def logbook_add(request, id):
    if request.method == 'POST':
        form = LogbookAddForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LogbookAddForm()
        form.fields['clinic'].queryset = Clinic.objects.filter(pk=id)
    context = {'form': form}
    return render(request, 'registry/logbook_add.html', context)

def profile(request):
    profile= []
    context = {'profile': profile}
    return render(request, 'registry/profile.html', context)


def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ProfileEditForm()
    context = {'form': form}
    return render(request, 'registry/profile_edit.html', context)


















