from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from registry.models import Region, District, Locality, Clinic, Disease, Vaccine, Logbook


def calendar(request):
    context = {}
    return render(request, 'info/calendar.html', context)


def clinics(request):
    if request.method == 'POST':
        form = ClinicsSearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['locality'] != '':
                clinics = Clinic.objects.filter(locality__locality=form.cleaned_data['locality'])
            elif form.cleaned_data['district'] != '':
                form.fields['locality'].queryset = Locality.objects.filter(district__district = form.cleaned_data['district'])
                clinics = Clinic.objects.filter(locality__district__district=form.cleaned_data['district'])
            elif form.cleaned_data['region'] != '':
                form.fields['district'].queryset = District.objects.filter(region__region = form.cleaned_data['region'])
                clinics = Clinic.objects.filter(licality__district__region__region = form.cleaned_data['region'])
            else:
                clinics = Clinic.objects.all()
    else:
        form = ClinicsSearchForm()
        clinics = Clinic.objects.all()
    context = {'clinics': clinics, 'form': form}
    return render(request, 'info/clinics.html', context)


def clinic(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    context = {'clinic': clinic}
    return render(request, 'info/clinic.html', context)


def vaccines(request):
    vaccines = Vaccine.objects.all()
    context = {'vaccines': vaccines}
    return render(request, 'info/vaccines.html', context)

def vaccine(request, id):
    vaccine = get_object_or_404(Vaccine, pk=id)
    context = {'vaccine': vaccine}
    return render(request, 'info/vaccine.html', context)

