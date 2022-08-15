from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters import rest_framework as filters



class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','isDelete')# 'date','services', 
    
    def list(self, request):
        queryset = models.Orders.objects.filter(isDelete=False)
        serializer = serializers.OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None): #returns single object
        id = pk
        if id is not None:
            queryset = models.Orders.objects.get(id=id)
            serializer = serializers.OrderSerializer(queryset)
        return Response({'success':True, 'msg':'Data retrieved', 'data':serializer.data})
        
    def create(self, request):
        serializer = serializers.OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Data Created', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # def create(self, request):
    #     services = request.data.pop('services')
    #     order_items = request.data.pop('order_items')
    #     order = models.Orders.objects.create(**request.data)
    #     for service in services:
    #         models.Services.objects.create(order=order, **service)
    #     for order_item in order_items:
    #         models.OrderItems.objects.create(order=order, **order_item)
    #     return Response(serializers.OrdersSerializer(order).data)
    

    def update(self, request, pk=None):
        order = self.get_object()
        if order.isDelete:
            return Response({'success':False, "message": "cannot update a deleted order"}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, pk)
        
    def destroy(self, request,pk):
        id=pk
        queryset= models.Orders.objects.get(pk=id)
        queryset.isDelete = True
        queryset.save()
        return Response({'success':True, 'msg':'Data Deleted'})

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServiceSerializer


# class OrderDetailViewSet(viewsets.ModelViewSet):
#     queryset = models.Orders.objects.all()
#     serializer_class = serializers.OrderDetailSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemSerializer

    def list(self, request):
        queryset = models.OrderItems.objects.all()
        serializer = serializers.OrderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None): #returns single object
        id = pk
        if id is not None:
            queryset = models.OrderItems.objects.get(id=id)
            serializer = serializers.OrderItemSerializer(queryset)
        return Response({'success':True, 'msg':'Data retrieved', 'data':serializer.data})
        
    def create(self, request):
        serializer = serializers.OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'msg':'Data Created', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
