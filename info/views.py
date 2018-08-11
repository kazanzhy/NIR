from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from registry.models import Region, District, Locality, Clinic, Disease, Vaccine, Logbook
from .forms import ClinicsSearchForm, VaccinesSearchForm


def calendar(request):
    context = {}
    return render(request, 'info/calendar.html', context)


def clinics(request):
    if request.method == 'POST':
        form = ClinicsSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['region'] is not None:
                form.fields['district'].queryset = District.objects.filter(region = form.cleaned_data['region'])
                form.fields['locality'].queryset = Locality.objects.filter(district__region = form.cleaned_data['region'])
                clinics = Clinic.objects.filter(locality__district__region = form.cleaned_data['region'])
            elif form.cleaned_data['district'] is not None:
                form.fields['locality'].queryset = Locality.objects.filter(district = form.cleaned_data['district'])
                clinics = Clinic.objects.filter(locality__district = form.cleaned_data['district'])
            elif form.cleaned_data['locality'] is not None:
                clinics = Clinic.objects.filter(locality = form.cleaned_data['locality'])
            else:
                clinics = Clinic.objects.all()
    else:
        form = ClinicsSearchForm()
        clinics = Clinic.objects.all()
    context = {'clinics': clinics, 'form': form}
    return render(request, 'info/clinics.html', context)


def clinic(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    vaccines = Logbook.objects.filter(clinic=clinic)
    context = {'clinic': clinic, 'vaccines': vaccines}
    return render(request, 'info/clinic.html', context)


def vaccines(request):
    if request.method == 'POST':
        form = VaccinesSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['disease'] is not None:
                vaccines = Vaccine.objects.filter(disease = form.cleaned_data['disease'])
            else:
                vaccines = Vaccine.objects.all()
    else:
        form = VaccinesSearchForm()
        vaccines = Vaccine.objects.all()
    context = {'vaccines': vaccines, 'form': form}
    return render(request, 'info/vaccines.html', context)

def vaccine(request, id):
    vaccine = get_object_or_404(Vaccine, pk=id)
    context = {'vaccine': vaccine}
    return render(request, 'info/vaccine.html', context)

