from rest_framework import serializers
from django.http import HttpRequest
from . models import Patient


class PatientsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient 
        fields = '__all__'

class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('pet_name','pet_type', 'owner_name', 'owner_phone_number', 'owner_address')
    

    pet_name = serializers.CharField(required=True)
    pet_type = serializers.CharField(required=True)
    owner_address = serializers.CharField(required=True)
    owner_name = serializers.CharField(required=True)
    owner_phone_number = serializers.CharField(required=True, min_length=9,max_length=11)

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def create(self, validated_data):
        if validated_data.get('pet_name') is None:
            pet_name = ''
        else:
            pet_name = validated_data.get('pet_name')
        if validated_data.get('owner_address') is None:
            owner_address = ''
        else:
            owner_address = validated_data.get('owner_address')
        if validated_data.get('pet_type') is None:
            pet_type = ''
        else:
            pet_type = validated_data.get('pet_type')
        if validated_data.get('owner_name') is None:
            owner_name = ''
        else:
            owner_name = validated_data.get('owner_name')
        if validated_data.get('owner_phone_number') is None:
            owner_phone_number = ''
        else:
            owner_phone_number = validated_data.get('owner_phone_number')
        patientCred = Patient(
            pet_name=validated_data.get('pet_name'),
            pet_type=validated_data.get('pet_type'),
            owner_address=validated_data.get('owner_address'),
            owner_name=validated_data.get('owner_name'),
            owner_phone_number=validated_data.get('owner_phone_number'),
        )
        patientCred.save()
        request = self._get_request()
        patientList = validated_data.get('patient')
        if patientList is not None:
            data = {"pet_name": pet_name,"pet_type": pet_type, "owner_name": owner_name,"owner_address":owner_address,'owner_phone_number':owner_phone_number}
            patients_credentials = PatientCredentialsSerializer(data=data)
            if patients_credentials.is_valid():
                patients_credentials.save()
            else:
                patientCred.delete()
                raise serializers.ValidationError(
                    (patientCred.errors))
        setup_patient(request, patientCred, [])
        return patientCred

    def save(self, request):
        """rest_auth passes request so we must override to accept it"""
        return super().save()







