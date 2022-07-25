from django.contrib import admin
from pets.models import Patient
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['pet_type', 'owner_name', 'owner_phone_number', 'owner_address']