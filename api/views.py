from django.http import JsonResponse

from registry.models import *


def regions(request):
    '''
    Return all regions in database as list of dicts
    '''
    # Get objects from database
    regions = Region.objects.all()
    # Convert queryset to list of dicts
    data = {region.id: region.region for region in regions}
    return JsonResponse(data)


def districts(request):
    '''
    Return districts of selected region. If region is't selected return all districts
    '''
    # Get region id or None
    region = request.GET.get('region', None)
    # Get objects from database
    try:
        region = int(region)
    except:
        districts = District.objects.all()
    else:
        districts = District.objects.filter(region=region)
    # If all is right convert queryset to dict
    data = {district.id: district.district for district in districts}
    return JsonResponse(data)

def localities(request):
    '''
    Return localities of selected district. If district is't selected return all localities
    '''
    # Get district id or None
    district = request.GET.get('district', None)
    # Get objects from database
    try:
        district = int(district)
    except:
        localities = Locality.objects.all()
    else:
        localities = Locality.objects.filter(district=district)
    # If all is right convert queryset to dict
    data = {locality.id: locality.locality for locality in localities}
    return JsonResponse(data)

def clinics(request):
    '''
    Return clinics of selected locality. If locality is't selected return all clinics
    '''
    # Get locality id or None
    locality = request.GET.get('locality', None)
    # Get objects from database
    try:
        locality = int(locality)
    except:
        clinics = Clinic.objects.all()
    else:
        clinics = Clinic.objects.filter(locality=locality)
    # If all is right convert queryset to dict
    data = {clinic.id: clinic.clinic for clinic in clinics}
    return JsonResponse(data)


def doctors(request):
    '''
    Return doctors of selected clinic. If clinic is't selected return all doctors
    '''
    # Get clinic id or None
    clinic = request.GET.get('clinic', None)
    # Get objects from database
    try:
        clinic = int(clinic)
    except:
        doctors = Doctor.objects.all()
    else:
        doctors = Doctor.objects.filter(clinic=clinic)
    # If all is right convert queryset to dict
    data = {doctor.id: '{} {} {}'.format(doctor.lastname, doctor.firstname, doctor.patronymic) for doctor in doctors}
    return JsonResponse(data)

def patients(request):
    '''
    Return patients with selected name. If name is't selected return all patients
    '''
    # Get patient's firstname, patronymic, lastname or None
    firstname = request.GET.get('firstname', '')
    patronymic = request.GET.get('patronymic', '')
    lastname = request.GET.get('lastname', '')
    # Get objects from database
    patients = Patient.objects.filter(firstname__firstname__icontains=firstname, patronymic__patronymic__icontains=patronymic, lastname__lastname__icontains=lastname)
    # If all is right convert queryset to list of dicts
    data = list(objects.values('id', 'firstname__firstname', 'patronymic__patronymic', 'lastname__lastname')) 
    return JsonResponse({"data": data})
    # If all is right convert queryset to dict
    data = {patient.id: '{} {} {}'.format(patient.lastname, patient.firstname, patient.patronymic) for patient in patients}
    return JsonResponse(data)

def vaccines(request):
    '''
    Return return all vaccines in database as list of dicts
    '''
    # Get objects from database
    vaccines = Vaccine.objects.all()
    # If all is right convert queryset to dict
    data = {vaccine.id: '{} ({}, {})'.format(vaccine.vaccine, vaccine.manufacturer, vaccine.country) for vaccine in vaccines}
    return JsonResponse(data)

def diseases(request):
    '''
    Return all diseases in database as list of dicts
    '''
    # Get objects from database
    diseases = Disease.objects.all()
    # If all is right convert queryset to dict
    data = {disease.id: disease.disease for disease in diseases}
    return JsonResponse(data)











