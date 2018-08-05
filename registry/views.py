from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from .models import *
from .forms import *

def clinics(request):
    pass
def clinic(request, id):
    pass
def clinic_add(request):
    pass
def clinic_update(request):
    pass
def clinic_delete(request):
    pass




def patients(request):
    pass

def doctors(request):
    pass




def immunizations(request):
    pass

def logbook(request):
    pass
