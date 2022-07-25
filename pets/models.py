from django.db import models

# Create your models here.
class Patient(models.Model):
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