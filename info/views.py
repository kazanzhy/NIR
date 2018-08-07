from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from registry.models import Region, District, Locality, Clinic, Disease, Vaccine, Logbook


def calendar(request):
    pass


def clinics(request):
    clinics = Clinic.objects.all()
    context = {'clinics': clinics}
    return render(request, 'info/clinics.html', context)


def clinic(request, id):
    pass


def vaccines(request):
    pass


def vaccine(request, id):
    pass

