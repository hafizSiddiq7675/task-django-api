from pets.viewsets import  PatientViewset, PatientAppointmentViewset,UnPaidAppointmentViewSet, AppointmentsForDayViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patient',PatientViewset, basename='Patient')
router.register('patient-appointment', PatientAppointmentViewset)
router.register('unpaid-appointment', UnPaidAppointmentViewSet)
router.register('appointmentforday',AppointmentsForDayViewSet, basename='AppointmentForDay')