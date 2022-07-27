from rest_framework import viewsets
from . import models
from . import serializers
from pets.pagination import CustomPageNumberPagination

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    pagination_class = CustomPageNumberPagination
    serializer_class = serializers.PatientSerializer
    
class PatientAppointmentViewset(viewsets.ModelViewSet):
    queryset = models.PatientAppointment.objects.all()
    pagination_class = CustomPageNumberPagination
    serializer_class = serializers.PatientAppointmentSerializer
    