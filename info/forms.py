from django import forms
from registry.models import Region, District, Locality, Disease


class ClinicsSearchForm(forms.Form):
    region = forms.ModelChoiceField(queryset = Region.objects.all(), required=False, label='Область')
    district = forms.ModelChoiceField(queryset = District.objects.all(), required=False, label='Район')
    locality = forms.ModelChoiceField(queryset = Locality.objects.all(), required=False, label='Населений пункт')
    
    
class VaccinesSearchForm(forms.Form):
    disease = forms.ModelChoiceField(queryset = Disease.objects.all(), required=False, label='Захворювання')
