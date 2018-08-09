from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from registry.models import Region, District, Locality, Clinic, Disease, Vaccine, Logbook


def calendar(request):
    context = {}
    return render(request, 'info/calendar.html', context)


def clinics(request):
    clinics = Clinic.objects.all()
    context = {'clinics': clinics}
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

