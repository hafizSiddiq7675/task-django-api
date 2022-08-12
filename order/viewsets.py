from rest_framework import viewsets
from . import models
from . import serializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrderSerializer

