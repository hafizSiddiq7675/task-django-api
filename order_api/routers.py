from rest_framework import routers
from order import viewsets

router = routers.DefaultRouter()


router.register('order/orderviewset/', viewsets.OrderViewSet)
