from django.urls import path
from .views import PatientsList

urlpatterns = [
    path('patients/', PatientsList.as_view(), name='patientslist'),

]