from rest_framework import serializers
from .models import Patient

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
    id = serializers.IntegerField()
    pet_name = serializers.CharField(required=True)
    pet_type = serializers.CharField(required=True)
    owner_address = serializers.CharField(required=True)
    owner_name = serializers.CharField(required=True)
    owner_phone_number = serializers.CharField(required=True, min_length=9,max_length=11)

