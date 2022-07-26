from pets.viewsets import  PatientViewset, PatientAppointmentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patient',PatientViewset, basename='Patient')
router.register('patient-appointment', PatientAppointmentViewset)