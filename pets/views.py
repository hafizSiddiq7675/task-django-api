# from django.shortcuts import render
from pets.models import Patient
from . serializers import PatientsListSerializer
# from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class PatientsList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # patients = Patient.objects.all()
        patients = Patient.objects.all()
        serializer = PatientsListSerializer(patients, many=True)
        return Response(serializer.data)
    
    
    
    
    
    
    

#     def post(self, request):
#         serializer = PatientsListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)