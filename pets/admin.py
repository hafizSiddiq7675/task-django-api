from django.contrib import admin
from pets.models import Patient, PatientAppointment
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['pet_name','pet_type', 'owner_name', 'owner_phone_number', 'owner_address']
    
@admin.register(PatientAppointment)
class PatientAppointmentAdmin(admin.ModelAdmin):
    list_display = ['appointment_start_time','appointment_end_time', 'description', 'payment_type', 'unpaid_amount','total_amount']