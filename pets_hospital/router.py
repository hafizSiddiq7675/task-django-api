from pets.viewsets import   PatientViewset, PatientAppointmentViewset, TotalAmountSumViewSet, UnPaidAppointmentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patient',PatientViewset, basename='Patient')
router.register('patient-appointment', PatientAppointmentViewset)
router.register('unpaid-appointment', UnPaidAppointmentViewSet)