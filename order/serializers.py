from rest_framework import serializers
from .models import OrderItem, Order, Service




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id','price','quantity','service_id','order_id']#,'service_id','order_id'
        # depth = 1

