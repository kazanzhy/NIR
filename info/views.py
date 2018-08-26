from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator

from registry.models import Region, District, Locality, Clinic, Disease, Vaccine, Logbook
from registry.forms import ClinicsSearchForm, VaccinesSearchForm


def calendar(request):
    context = {}
    return render(request, 'info/calendar.html', context)


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
    return render(request, 'info/clinics.html', context)


def clinic(request, id):
    clinic = get_object_or_404(Clinic, pk=id)
    vaccines = Logbook.objects.filter(clinic=clinic)
    context = {'clinic': clinic, 'vaccines': vaccines}
    return render(request, 'info/clinic.html', context)


def vaccines(request):
    form = VaccinesSearchForm(request.GET)
    if form.is_valid() and form.cleaned_data['disease'] is not None:
        vaccines = Vaccine.objects.filter(disease=form.cleaned_data['disease'])
    else:
        vaccines = Vaccine.objects.all()
    context = {'vaccines': vaccines, 'form': form}
    return render(request, 'info/vaccines.html', context)

def vaccine(request, id):
    vaccine = get_object_or_404(Vaccine, pk=id)
    context = {'vaccine': vaccine}
    return render(request, 'info/vaccine.html', context)

