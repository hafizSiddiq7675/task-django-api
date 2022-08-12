from rest_framework import serializers
from .models import OrderItems, Orders, Services



class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Orders
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = '__all__'

    def get_services(self, obj):
        qs = obj.services.all()
        return qs