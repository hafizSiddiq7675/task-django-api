from pets.viewsets import  PatientViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('patients',PatientViewset)