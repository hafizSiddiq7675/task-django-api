from pets.viewsets import   PatientViewset, PatientAppointmentViewset, TotalAmountSumViewSet, UnPaidAppointmentViewSet, UnpaidAmountSumViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patient',PatientViewset, basename='Patient')
router.register('patient-appointment', PatientAppointmentViewset)
router.register('unpaid-appointment', UnPaidAppointmentViewSet)
router.register('total-amount-sum',TotalAmountSumViewSet, basename='totalamountsum')
# router.register('unpaid-amount-sum',UnpaidAmountSumViewSet, basename='unpaidamountsum')
# router.register('unpaid-amount-sum',UnPaidAmountPaidSumViewSet, basename='unpaidamountsum')