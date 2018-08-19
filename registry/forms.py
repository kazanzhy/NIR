from django import forms
from registry.models import Region, District, Locality, Disease, Clinic

    
class VaccinesSearchForm(forms.Form):
    disease = forms.ModelChoiceField(label='Захворювання', queryset = Disease.objects.all(), required=False)

class ClinicsSearchForm(forms.Form):
    region = forms.ModelChoiceField(label='Область', queryset = Region.objects.all(), required=False)
    district = forms.ModelChoiceField(label='Район', queryset = District.objects.all(), required=False)
    locality = forms.ModelChoiceField(label='Населений пункт', queryset = Locality.objects.all(), required=False)

class PatientsSearchForm(forms.Form):
    lastname = forms.CharField(label='Фамілія', max_length=32)
    firstname = forms.CharField(label='Ім\'я', max_length=32)
    patronymic = forms.CharField(label='По-батькові', max_length=32)

class DoctorsSearchForm(forms.Form):
    lastname = forms.CharField(label='Фамілія', max_length=32)
    firstname = forms.CharField(label='Ім\'я', max_length=32)
    patronymic = forms.CharField(label='По-батькові', max_length=32)

class ClinicAddForm(forms.Form):
    region = forms.ModelChoiceField(label='Область', queryset = Region.objects.all(), required=False)
    district = forms.ModelChoiceField(label='Район', queryset = District.objects.all(), required=False)
    locality = forms.ModelChoiceField(label='Населений пункт', queryset = Locality.objects.all())
    clinic = forms.CharField(label='Назва', max_length=64)
    logo = forms.ImageField(label='Логотип', required=False)
    info = forms.CharField(label='Інформація', max_length=265, required=False, widget=forms.Textarea)

class DoctorAddForm(forms.Form):
    clinic = forms.ModelChoiceField(label='Клініка', queryset = Clinic.objects.all())
    lastname = forms.CharField(label='Фамілія', max_length=32)
    firstname = forms.CharField(label='Ім\'я', max_length=32)
    patronymic = forms.CharField(label='По-батькові', max_length=32)

class PatientAddForm(forms.Form):
    lastname = forms.CharField(label='Фамілія', max_length=32)
    firstname = forms.CharField(label='Ім\'я', max_length=32)
    patronymic = forms.CharField(label='По-батькові', max_length=32)
    sex = forms.ChoiceField(label='Стать', choices = ((True,'Чоловіча'), (False, 'Жіноча')))
    birth = forms.DateField(label='Дата народження', widget=forms.widgets.DateInput(format='%d.%m.%Y'))
    phone = forms.CharField(label='Телефон', initial= '+380', max_length=17)


class ImmunizationAddForm(forms.Form):
    lastname = forms.CharField(label='Фамілія', max_length=32)
    firstname = forms.CharField(label='Ім\'я', max_length=32)
    patronymic = forms.CharField(label='По-батькові', max_length=32)
    sex = forms.ChoiceField(label='Стать', choices = ((True,'Чоловіча'), (False, 'Жіноча')))
    birth = forms.DateField(label='Дата народження', input_formats = ['%d.%m.%Y', '%d,%m,%Y', '%d,%m,%Y'])
    phone = forms.CharField(label='Телефон', initial= '+380', max_length=17)

