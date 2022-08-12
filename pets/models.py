from django.db import models
from django.utils.translation import gettext_lazy as _


class Patient(models.Model):

    pet_name = models.CharField(max_length=255)
    cat = 'cat'
    dog = 'dog'
    bird = 'bird'
    PET_TYPE_CHOICES = [
        (cat, cat),
        (dog, dog),
        (bird, bird),
    ]
    pet_type = models.CharField("Select Pet Type", choices=PET_TYPE_CHOICES, null=False, max_length=15)
    owner_name = models.CharField("Owner Name",max_length=255)
    owner_address = models.CharField("Owner Address", max_length=255, null=True, blank=True)
    owner_phone_number = models.CharField("phone", max_length=11, blank=False, default='')
    
    
    def __str__(self):
        return str(self.id)
    
    
class PatientAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True) #, null=True)
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
    paid_amount = models.DecimalField(_("Enter amount paid"), max_digits=5, decimal_places=2, null=True)
    unpaid_amount = models.DecimalField(_("Enter unpaid amount"), max_digits=5, decimal_places=2, null=True)
    total_amount = models.DecimalField(_("Enter Total amount"), max_digits=5, decimal_places=2, null=True)
    
    
    def __str__(self):
        return str(self.id)
