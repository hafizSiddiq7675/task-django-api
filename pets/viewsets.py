from rest_framework import viewsets
from . import models
from . import serializers
from pets.CustomPagination import CustomPageNumberPagination

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404




# *****************************************  PatientAppointmentViewset  *****************************************
    
class PatientAppointmentViewset(viewsets.ModelViewSet):


    serializer_class = serializers.PatientAppointmentSerializer
    queryset = models.PatientAppointment.objects.all()
    pagination_class = CustomPageNumberPagination
    
    
    def list(self,request): #returns list
        patient_appointment = models.PatientAppointment.objects.all()   
        serializer = serializers.PatientAppointmentSerializer(patient_appointment, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None): #returns single object
        id = pk
        if id is not None:
            patient_appointment = models.PatientAppointment.objects.get(id=id)
            serializer = serializers.PatientAppointmentSerializer(patient_appointment)
        return Response({'success':True, 'msg':'Data retrieved', 'data':serializer.data})


    # def create(self, request):
    #     serializer = serializers.PatientAppointmentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'success':True, 'msg':'Data Created', 'data':serializer.data}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, *args, **kwargs):
        patient_appointment_data = request.data
        
        appointment = models.PatientAppointment.objects.create(
        appointment_start_time=patient_appointment_data['appointment_start_time'],
        appointment_end_time=patient_appointment_data['appointment_end_time'],
        description=patient_appointment_data['description'],
        payment_type=patient_appointment_data['payment_type'],
        unpaid_amount=patient_appointment_data['unpaid_amount'],
        total_amount=patient_appointment_data['total_amount'],
        patient_id=models.Patient.objects.get(id=patient_appointment_data['patient_id']),
        )
        appointment.save()
        serializer=serializers.PatientAppointmentSerializer(appointment)
        return Response(serializer.data)


    def update(self, request, pk):
        id = pk
        patient_appointment= models.PatientAppointment.objects.get(pk=id)
        serializer = serializers.PatientAppointmentSerializer(patient_appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Data Updated', 'data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk):
        id = pk
        patient_appointment= models.PatientAppointment.objects.get(pk=id)
        serializer = serializers.PatientAppointmentSerializer(patient_appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Partial Data Updated', 'data':serializer.data})
        return Response(serializer.errors)
        
        
    def destroy(self, request,pk):
        id=pk
        patient= models.PatientAppointment.objects.get(pk=id)
        patient.delete()
        return Response({'success':True, 'msg':'Data DEleted'})
    
    
# *****************************************  PatientViewset  *****************************************
class PatientViewset(viewsets.ModelViewSet): 
    
    serializer_class = serializers.PatientSerializer
    queryset = models.Patient.objects.all()
    pagination_class = CustomPageNumberPagination
    
    
    def list(self,request): #returns list
        patient = models.Patient.objects.all()   
        serializer = serializers.PatientSerializer(patient, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None): #returns single object
        try:
            # id = pk
            if id is not None:
                patient = models.Patient.objects.get(id=id)
                serializer = serializers.PatientSerializer(patient)
            return Response({'success':True, 'msg':'Data retrieved', 'data':serializer.data})
        except Exception as e :
            return Response({'error':str(e)})

    
    def create(self, request):
        serializer = serializers.PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Data Created', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        patient= models.Patient.objects.get(pk=id)
        serializer = serializers.PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Data Updated', 'data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk):
        id = pk
        patient= models.Patient.objects.get(pk=id)
        serializer = serializers.PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Partial Data Updated', 'data':serializer.data})
        return Response(serializer.errors)
     
        
    def destroy(self, request,pk):
        id=pk
        patient= models.Patient.objects.get(pk=id)
        patient.delete()
        return Response({'success':True, 'msg':'Data DEleted'})

        
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    # def retrieve(self, request, pk=None): #returns single object
    #     try:
    #         id = pk
    #         if id is not None:
    #             patient = models.Patient.objects.get(id=id)
    #             serializer = serializers.PatientSerializer(patient)
    #             patient_appointment = models.PatientAppointment.objects.get(id=patient)
    #             serializer_appointment = serializers.PatientAppointmentSerializer(patient_appointment)
    #         return Response({'success':True, 'msg':'Data retrieved', 'data':serializer.data,'appointment':serializer_appointment.data})
    #     except Exception as e:
    #         return str(e)


    # def retrieve(self, request, pk=None): #returns single object
    #     id = pk
    #     if id is not None:
    #         patient = models.Patient.objects.get(id=id)
    #         serializer = serializers.PatientSerializer(patient)
    #         patient_appointment = models.PatientAppointment.objects.get(id=patient)
    #         serializer_appointment = serializers.PatientAppointmentSerializer(patient_appointment)
    #     return Response({'success':True, 'msg':'Data retrieved', 'data':serializer.data,'appointment':serializer_appointment.data})
    
    
    
# class PatientViewset(viewsets.ModelViewSet):
#     queryset = models.Patient.objects.all()
    # pagination_class = CustomPageNumberPagination
#     serializer_class = serializers.PatientSerializer
    
# class PatientAppointmentViewset(viewsets.ModelViewSet):
#     queryset = models.PatientAppointment.objects.all()
#     pagination_class = CustomPageNumberPagination
#     serializer_class = serializers.PatientAppointmentSerializer
