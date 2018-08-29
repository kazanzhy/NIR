from django import forms

from registry.models import *


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
    clinic = forms.CharField(label='Назва', max_length=64, widget=forms.TextInput(attrs={'size':40}))
    logo = forms.ImageField(label='Логотип', required=False)
    info = forms.CharField(label='Інформація', max_length=265, required=False, widget=forms.Textarea(attrs={'rows':4, 'cols':40}))

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
    patient = forms.ModelChoiceField(label='Пацієнт', queryset = Patient.objects.all())
    doctor = forms.ModelChoiceField(label='Доктор', queryset = Doctor.objects.all())
    vaccine = forms.ModelChoiceField(label='Вакцина', queryset = Vaccine.objects.all())
    series = forms.CharField(label='Серія', max_length=32)
    dose = forms.FloatField(label='Доза')
    general_reaction = forms.CharField(label='Загальна реакція', max_length=128, required=False)
    local_reaction = forms.CharField(label='Місцева реакція', max_length=128, required=False)
    contraindications = forms.CharField(label='Протипоказання', max_length=128, required=False)
    date = forms.DateField(label='Дата', widget=forms.widgets.DateInput(format='%d.%m.%Y'))

class LogbookAddForm(forms.Form):
    clinic = forms.ModelChoiceField(label='Клініка', required=False, queryset = Clinic.objects.all())
    vaccine = forms.ModelChoiceField(label='Вакцина', required=False, queryset = Vaccine.objects.all())
    series = forms.CharField(label='Серія', max_length=32)
    doses = forms.IntegerField(label='Кількість доз')
    date = forms.DateField(label='Дата', widget=forms.SelectDateWidget(), input_formats=('%d.%m.%Y'))

class ProfileEditForm(forms.Form):
    region = forms.ModelChoiceField(label='Область', queryset = Region.objects.all(), required=False)
    district = forms.ModelChoiceField(label='Район', queryset = District.objects.all(), required=False)
    locality = forms.ModelChoiceField(label='Населений пункт', queryset = Locality.objects.all(), required=False)
    clinic = forms.ModelChoiceField(label='Клініка', required=False, queryset = Clinic.objects.all())






