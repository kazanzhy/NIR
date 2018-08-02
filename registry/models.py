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
        """
        String for representing the Model object.
        """
        return self.name

class Patronymic(models.Model):
    """
    Model representing a Patronymic name.
    """
    name = models.CharField(max_length=32)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Lastname(models.Model):
    """
    Model representing a Last name.
    """
    name = models.CharField(max_length=32)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Region(models.Model):
    """
    Model representing a Region.
    """
    region = models.CharField(max_length=32)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.region

class District(models.Model):
    """
    Model representing a District.
    """
    district = models.CharField(max_length=32)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.district

class Locality(models.Model):
    """
    Model representing a Locality.
    """
    locality = models.CharField(max_length=32)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.locality

class Clinic(models.Model):
    """
    Model representing a Clinic.
    """
    clinic = models.CharField(max_length=64)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.clinic

class Patient(models.Model):
    """
    Model representing a Patient.
    """
    firstname = models.ForeignKey(Firstname, on_delete=models.SET_NULL, null=True, blank=True)
    patronymic = models.ForeignKey(Patronymic, on_delete=models.SET_NULL, null=True, blank=True)
    lastname = models.ForeignKey(Lastname, on_delete=models.SET_NULL, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    sex = models.BooleanField() # 1 for Male and 0 for Female
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{} {} {}, {}'.format(self.firstname, self.patronymic, self.lastname, self.birth)

class Doctor(models.Model):
    """
    Model representing a Doctor.
    """
    firstname = models.ForeignKey(Firstname, on_delete=models.SET_NULL, null=True, blank=True)
    patronymic = models.ForeignKey(Patronymic, on_delete=models.SET_NULL, null=True, blank=True)
    lastname = models.ForeignKey(Lastname, on_delete=models.SET_NULL, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'Dr. {} {} {} ({})'.format(self.firstname, self.patronymic, self.lastname, self.clinic)

class Disease(models.Model):
    """
    Model representing a Disease.
    """
    disease = models.CharField(max_length=32)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.disease

class Manufacturer(models.Model):
    """
    Model representing a Manufacturer.
    """
    manufacturer = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{} ({})'.format(self.manufacturer, self.country)


class Vaccine(models.Model):
    """
    Model representing a Vaccine.
    """
    vaccine = models.CharField(max_length=32)
    disease = models.ManyToManyField(Disease, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.vaccine


class Series(models.Model):
    """
    Model representing a Series.
    """
    series = models.CharField(max_length=32)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True, blank=True)
    expiration = models.DateField(null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.series


class Logbook(models.Model):
    """
    Model representing a Logbook.
    """
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    doses = models.IntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.localdate)
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{}: {} #{}. {}'.format(self.clinic, self.series, self.doses, self.date)


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
        """
        String for representing the Model object.
        """
        return '{} - {} - {}'.format(self.patient, self.series, self.doctor)



























