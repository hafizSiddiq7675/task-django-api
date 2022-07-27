from rest_framework import serializers
from .models import Patient, PatientAppointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'pet_name',
            'pet_type',
            'owner_address',
            'owner_name',
            'owner_phone_number',
        )
    pet_name = serializers.CharField(required=True)
    pet_type = serializers.CharField(required=True)
    owner_address = serializers.CharField(required=True)
    owner_name = serializers.CharField(required=True)
    owner_phone_number = serializers.CharField(required=True, min_length=9,max_length=11)


class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAppointment
        fields = (
            'id',
            'appointment_start_time',
            'appointment_end_time',
            'description',
            'payment_type',
            'unpaid_amount',
            'total_amount',
            'patient_id'
        )
    appointment_start_time = serializers.DateTimeField(required=True)
    appointment_end_time = serializers.DateTimeField(required=True)
    description = serializers.CharField(required=False)
    payment_type = serializers.CharField(required=True)
    unpaid_amount = serializers.IntegerField(required=True)
    total_amount = serializers.IntegerField(required=True)