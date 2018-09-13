from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver



class Firstname(models.Model):
    """
    Model representing a First name.
    """
    firstname = models.CharField(max_length=32)
    def __str__(self):
        return self.firstname
    class Meta:
        verbose_name = "Ім'я"
        verbose_name_plural = "Імена"


class Patronymic(models.Model):
    """
    Model representing a Patronymic name.
    """
    patronymic = models.CharField(max_length=32)
    def __str__(self):
        return self.patronymic
    class Meta:
        verbose_name = "По-батькові"
        verbose_name_plural = "По-батькові"


class Lastname(models.Model):
    """
    Model representing a Last name.
    """
    lastname = models.CharField(max_length=32)
    def __str__(self):
        return self.lastname
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
        ordering = ['region']


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
        ordering = ['district']


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
        ordering = ['locality']


class Clinic(models.Model):
    """
    Model representing a Clinic.
    """
    clinic = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    info = models.TextField(max_length=265, blank=True, null=True)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.clinic

    def get_registry_url(self):
        return reverse('clinic', args=[str(self.id)])

    def get_info_url(self):
        return reverse('info_clinic', args=[str(self.id)])

    class Meta:
        verbose_name = "Клініка"
        verbose_name_plural = "Клініки"
        ordering = ['-id']


class Patient(models.Model):
    """
    Model representing a Patient.
    """
    firstname = models.ForeignKey(Firstname, on_delete=models.SET_NULL, null=True, blank=True)
    patronymic = models.ForeignKey(Patronymic, on_delete=models.SET_NULL, null=True, blank=True)
    lastname = models.ForeignKey(Lastname, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    sex = models.BooleanField() # 1 for Male and 0 for Female
    def __str__(self):
        return '{} {} {}, {}'.format(self.firstname, self.patronymic, self.lastname, self.birth)
    def get_registry_url(self):
        return reverse('patient', args=[str(self.id)])
    class Meta:
        verbose_name = "Пацієнт"
        verbose_name_plural = "Пацієнти"
        ordering = ['-id']


class Doctor(models.Model):
    """
    Model representing a Doctor.
    """
    firstname = models.ForeignKey(Firstname, on_delete=models.SET_NULL, null=True, blank=True)
    patronymic = models.ForeignKey(Patronymic, on_delete=models.SET_NULL, null=True, blank=True)
    lastname = models.ForeignKey(Lastname, on_delete=models.SET_NULL, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return 'Dr. {} {} {}'.format(self.firstname, self.patronymic, self.lastname)
    def get_registry_url(self):
        return reverse('doctor', args=[str(self.id)])
    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"
        ordering = ['-id']

class Disease(models.Model):
    """
    Model representing a Disease.
    """
    disease = models.CharField(max_length=32)
    disease_en = models.CharField(max_length=32)
    def __str__(self):
        return self.disease
    class Meta:
        verbose_name = "Захворювання"
        verbose_name_plural = "Захворювання"
        ordering = ['disease']


class Vaccine(models.Model):
    """
    Model representing a Vaccine.
    """
    vaccine = models.CharField(max_length=64, null=True, blank=True)
    vaccine_en = models.CharField(max_length=64, null=True, blank=True)
    manufacturer = models.CharField(max_length=32, null=True, blank=True)
    manufacturer_en = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=16, null=True, blank=True)
    country_en = models.CharField(max_length=16, null=True, blank=True)
    info =  models.CharField(max_length=256, null=True, blank=True)
    disease = models.ManyToManyField(Disease, blank=True)
    def __str__(self):
        return self.vaccine

    def get_info_url(self):
        return reverse('info_vaccine', args=[str(self.id)])

    class Meta:
        verbose_name = "Вакцина"
        verbose_name_plural = "Вакцини"
        ordering = ['vaccine']


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
        ordering = ['-id']


class Logbook(models.Model):
    """
    Model representing a Logbook.
    """
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    doses = models.PositiveSmallIntegerField(null=True, blank=True)
    arrival = models.BooleanField(null=True, blank=True)
    balance = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return '{}: {} #{}. {}'.format(self.clinic, self.series, self.doses, self.date)
    class Meta:
        verbose_name = "Запис у журналі"
        verbose_name_plural = "Журнал обліку"
        ordering = ['-id']


class Immunization(models.Model):
    """
    Model representing a Immunization.
    """
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    general_reaction = models.CharField(max_length=256, null=True, blank=True)
    local_reaction = models.CharField(max_length=256, null=True, blank=True)
    contraindications = models.CharField(max_length=256, null=True, blank=True)
    dose = models.FloatField(default=1)
    date = models.DateField(default=timezone.localdate)
    def __str__(self):
        return '{} - {} - {}'.format(self.patient, self.series, self.doctor)
    def get_registry_url(self):
        return reverse('immunization', args=[str(self.id)])
    class Meta:
        verbose_name = "Щеплення"
        verbose_name_plural = "Щеплення"
        ordering = ['-id']

class Profile(models.Model):
    """
    Model representing user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Standart User model
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, blank=True)
    token = models.CharField(max_length=32, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.user
    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"
'''
# This block for automated creation of profile-instance when new user registrated 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''


