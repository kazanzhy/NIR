from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Firstname(models.Model):
    """
    Model representing a First name.
    """
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Ім'я"
        verbose_name_plural = "Імена"


class Patronymic(models.Model):
    """
    Model representing a Patronymic name.
    """
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "По-батькові"
        verbose_name_plural = "По-батькові"


class Lastname(models.Model):
    """
    Model representing a Last name.
    """
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Фамілія"
        verbose_name_plural = "Фамілії"


class Region(models.Model):
    """
    Model representing a Region.
    """
    region = models.CharField(max_length=32)
    def __str__(self):
        return self.region
    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Області"


class District(models.Model):
    """
    Model representing a District.
    """
    district = models.CharField(max_length=32)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.district
    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Райони"


class Locality(models.Model):
    """
    Model representing a Locality.
    """
    locality = models.CharField(max_length=32)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.locality
    class Meta:
        verbose_name = "Населений пункт"
        verbose_name_plural = "Населені пункти"


class Clinic(models.Model):
    """
    Model representing a Clinic.
    """
    clinic = models.CharField(max_length=64)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.clinic
    class Meta:
        verbose_name = "Клініка"
        verbose_name_plural = "Клініки"


class Patient(models.Model):
    """
    Model representing a Patient.
    """
    firstname = models.ForeignKey(Firstname, on_delete=models.SET_NULL, null=True, blank=True)
    patronymic = models.ForeignKey(Patronymic, on_delete=models.SET_NULL, null=True, blank=True)
    lastname = models.ForeignKey(Lastname, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=17, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    sex = models.BooleanField() # 1 for Male and 0 for Female
    def __str__(self):
        return '{} {} {}, {}'.format(self.firstname, self.patronymic, self.lastname, self.birth)
    class Meta:
        verbose_name = "Пацієнт"
        verbose_name_plural = "Пацієнти"


class Doctor(models.Model):
    """
    Model representing a Doctor.
    """
    firstname = models.ForeignKey(Firstname, on_delete=models.SET_NULL, null=True, blank=True)
    patronymic = models.ForeignKey(Patronymic, on_delete=models.SET_NULL, null=True, blank=True)
    lastname = models.ForeignKey(Lastname, on_delete=models.SET_NULL, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return 'Dr. {} {} {} ({})'.format(self.firstname, self.patronymic, self.lastname, self.clinic)
    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"


class Disease(models.Model):
    """
    Model representing a Disease.
    """
    disease = models.CharField(max_length=32)
    def __str__(self):
        return self.disease
    class Meta:
        verbose_name = "Захворювання"
        verbose_name_plural = "Захворювання"


class Vaccine(models.Model):
    """
    Model representing a Vaccine.
    """
    vaccine = models.CharField(max_length=64, null=True, blank=True)
    manufacturer = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    info =  models.CharField(max_length=256, null=True, blank=True)
    disease = models.ManyToManyField(Disease, null=True, blank=True)
    def __str__(self):
        return self.vaccine
    class Meta:
        verbose_name = "Вакцина"
        verbose_name_plural = "Вакцини"


class Series(models.Model):
    """
    Model representing a Series.
    """
    series = models.CharField(max_length=32)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True, blank=True)
    expiration = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.series
    class Meta:
        verbose_name = "Серія"
        verbose_name_plural = "Серії"


class Logbook(models.Model):
    """
    Model representing a Logbook.
    """
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    doses = models.IntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.localdate)
    def __str__(self):
        return '{}: {} #{}. {}'.format(self.clinic, self.series, self.doses, self.date)
    class Meta:
        verbose_name = "Запис у журналі"
        verbose_name_plural = "Журнал обліку"

class Immunization(models.Model):
    """
    Model representing a Immunization.
    """
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    dose = models.IntegerField(default=1)
    date = models.DateField(default=timezone.localdate)
    def __str__(self):
        return '{} - {} - {}'.format(self.patient, self.series, self.doctor)
    class Meta:
        verbose_name = "Щеплення"
        verbose_name_plural = "Щеплення"

























