from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Patient(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    pet_name = models.CharField(max_length=255)
    cat = 'cat'
    dog = 'dog'
    bird = 'bird'
    PET_TYPE_CHOICES = [
        (cat, cat),
        (dog, dog),
        (bird, bird),
        # (cat, 'cat'),
        # (dog, 'dog'),
        # (bird, 'bird'),
    ]
    pet_type = models.CharField("Select Pet Type", choices=PET_TYPE_CHOICES, null=False, max_length=15)
    owner_name = models.CharField("Owner Name",max_length=255)
    owner_address = models.CharField("Owner Address", max_length=255, null=True, blank=True)
    owner_phone_number = models.CharField("phone", max_length=11, blank=False, default='')
    
    def __str__(self):
        return self.pet_name
    
class PatientAppointment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    appointment_start_time = models.DateTimeField(_("Appointment start time"), auto_now=False, auto_now_add=False)
    appointment_end_time = models.DateTimeField(_("Appointment end time"), auto_now=False, auto_now_add=False)
    description = models.CharField(_("Enter description"), max_length=1024)
    USD = 'USD'
    EUR = 'EUR'
    BITCOIN = 'BITCOIN'
    PAYMENT_TYPE_CHOICES = [
        (USD, USD),
        (EUR, EUR),
        (BITCOIN, BITCOIN),
    ]
    payment_type = models.CharField("Select payment Type", choices=PAYMENT_TYPE_CHOICES, null=False, max_length=15, default='USD')
    unpaid_amount = models.IntegerField(_("Enter unpaid amount"))
    total_amount = models.IntegerField(_("Enter total amount"))
    
    