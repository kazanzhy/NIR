from django.http import JsonResponse

from registry.models import *


def regions(request):
    '''
    Return all regions in database as list of dicts
    '''
    # Get objects from database
    objects = Region.objects.all()
    # Convert queryset to list of dicts
    data = list(objects.values('id', 'region')) 
    return JsonResponse({"data": data})


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
        objects = District.objects.all()
    else:
        objects = District.objects.filter(region=region)
    # If all is right convert queryset to list of dicts
    data = list(objects.values('id', 'district')) 
    return JsonResponse({"data": data})

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
        objects = Locality.objects.all()
    else:
        objects = Locality.objects.filter(district=district)
    # If all is right convert queryset to list of dicts
    data = list(objects.values('id', 'locality')) 
    return JsonResponse({"data": data})

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
        objects = Clinic.objects.all()
    else:
        objects = Clinic.objects.filter(locality=locality)
    # If all is right convert queryset to list of dicts
    data = list(objects.values('id', 'clinic')) 
    return JsonResponse({"data": data})

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
        objects = Doctor.objects.all()
    else:
        objects = Doctor.objects.filter(clinic=clinic)
    # If all is right convert queryset to list of dicts
    data = list(objects.values('id', 'firstname__firstname', 'patronymic__patronymic', 'lastname__lastname')) 
    return JsonResponse({"data": data})

def patients(request):
    '''
    Return patients with selected name. If name is't selected return all patients
    '''
    # Get patient's firstname, patronymic, lastname or None
    firstname = request.GET.get('firstname', '')
    patronymic = request.GET.get('patronymic', '')
    lastname = request.GET.get('lastname', '')
    # Get objects from database
    objects = Patient.objects.filter(firstname__firstname__icontains=firstname, patronymic__patronymic__icontains=patronymic, lastname__lastname__icontains=lastname)
    # If all is right convert queryset to list of dicts
    data = list(objects.values('id', 'firstname__firstname', 'patronymic__patronymic', 'lastname__lastname')) 
    return JsonResponse({"data": data})

def vaccines(request):
    '''
    Return return all vaccines in database as list of dicts
    '''
    # Get objects from database
    objects = Vaccine.objects.all()
    # Convert queryset to list of dicts
    data = list(objects.values('id', 'vaccine', 'manufacturer', 'country')) 
    return JsonResponse({"data": data})

def diseases(request):
    '''
    Return all diseases in database as list of dicts
    '''
    # Get objects from database
    objects = Disease.objects.all()
    # Convert queryset to list of dicts
    data = list(objects.values('id', 'disease')) 
    return JsonResponse({"data": data})












