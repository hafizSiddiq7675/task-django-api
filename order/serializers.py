from rest_framework import serializers
from .models import OrderItems, Orders, Services




# class OrderSerializer(serializers.Serializer):
#     class Meta:
#         model = Orders
#         fields = '__all__'
        
# class OrderSerializer(serializers.ModelSerializer):
#     services = serializers.SerializerMethodField()

#     class Meta:
#         model = Orders
#         fields = '__all__'

#     def get_services(self, obj):
#         qs = obj.services.all()
#         return qs


# class OrderSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = Orders
#         fields = ['id','date','services','order_items']
#         depth = 1

    # def get_services(self, obj):
    #     def __json__(self):
    #         return {
    #             'id': self.id,
    #             'name': self.name,
    #             'price': self.price,
    #     }


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'



class OrderItemSerializer(serializers.ModelSerializer):
    # order_id = serializers.CharField(source='order_id.id')

    class Meta:
        model = OrderItems
        fields = ['id','price','quantity']#,'service_id','order_id'
        # depth = 1
        
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id','date','services','order_items']
        depth = 1

    services = ServiceSerializer(many=True)
    order_items = OrderItemSerializer(many=True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# order = ServiceSerializer(source='order_id',read_only=True)
# class OrderDetailSerializer(serializers.ModelSerializer):
#     # services = ServiceSerializer(many=True)
#     # order_items = OrderItemSerializer(many=True)

#     class Meta:
#         model = Orders
#         fields = '__all__'
