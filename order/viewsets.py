from order.serializers import OrderItemSerializer, OrderSerializer
from .models import Order, OrderItem
from rest_framework.response import Response
import  json
from datetime import datetime, date, timedelta
from rest_framework import status, viewsets
from django_filters import rest_framework as filters
from django.db.models import Count


############################################ OrderViewSet ############################################

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def list(self, request):
        queryset = Order.objects.all().filter(isDelete=False)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        print("-------------------------------------------------------------------------------------------------")
        id = pk
        qs = Order.objects.filter(id=id).filter(isDelete=False)
        print('orderitems= '+ str(qs))
        print("-------------------------------------------------------------------------------------------------")
        if not qs:
            return Response({'error': "No query found!"})
        else:
            return Response({'Order':qs.values()})

    def create(self, request, *args, **kwargs):
        now = datetime.date.today() 
        order = Order.objects.create(date=now) 
        order.save()
        data = json.loads(request.body)
        for item in data:
            OrderItem.objects.create(
                order_id_id=order.id, 
                quantity=item.get("quantity"), 
                service_id_id=item.get("service_id"), 
                price=item.get("price")
            )
            print('items'+ str(item))
        return Response({"success":"True","msg":"order created"})
    
    def destroy(self, request,pk):
        id=pk
        print("id" + str(id))
        queryset= Order.objects.get(pk=id)
        queryset.isDelete = True
        queryset.save()
        return Response({'success':True, 'msg':'Data Deleted'})
    
    

############################################ OrderItemViewSet ############################################

class GetOrderItemViewSet(viewsets.ModelViewSet):
    lookup_field = "order_id_id"
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('order_id','service_id','quantity','price')
    
    def list(self, request):
        queryset = OrderItem.objects.filter(order_id__isDelete=False)
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        print("-------------------------------------------------------------------------------------------------")
        order_id = kwargs[self.lookup_field]
        qs = OrderItem.objects.filter(order_id_id=order_id).filter(order_id__isDelete=False)
        print('order_id= '+ order_id)
        print('orderitems= '+ str(qs))
        print("-------------------------------------------------------------------------------------------------")
        if not qs:
            return Response({'error': "No query found!"})
        else:
            return Response({'orderitems':qs.values()})
            # serializer = OrderItemSerializer(orderitems)
            # return Response(serializer.data)
    

    def update(self, request, *args, **kwargs):
        order = Order.objects.filter(id=kwargs[self.lookup_field]).filter(isDelete=False)
        if not order:
            return Response({'error': "No query found!"})
        else:
            print("order= "+ str(order))
            # qs = OrderItem.objects.filter(order_id_id=order, service_id_id=item.get("service_id"))
            # print('qs =' + str(qs))
            order_id = kwargs[self.lookup_field]
            qs = OrderItem.objects.filter(order_id_id=order_id)
            print('orderitems= '+ str(qs))
            qs.delete()
            print('order_id= '+ order_id)
            data = json.loads(request.body)
            print("DATA= "+ str(data))
            for item in data:
                qs =OrderItem.objects.create(
                    order_id_id=order_id,
                    quantity=item.get("quantity"),
                    service_id_id=item.get("service_id_id"), 
                    price=item.get("price")
                )
                print('items'+ str(item))
            return Response({"success":"True","msg":"order updated","items":(item)})



###################################### Total Orders in year, month and week ######################################
class TotalOrdersViewset(viewsets.ViewSet):
    serializer_class = OrderSerializer
    def list(self, request):
        try:
            params = self.request.query_params
            type = params.get('type')
            print('type= '+str(type))
            if type is None:
                return Response({"success": False, "message": "type param describing week, month or year is missing."}, status=400)
            elif type == 'month':
                qs = Order.objects.filter(date__month=datetime.now().month).count()
                return Response({'Number of orders this month': qs})
            elif type == 'year':
                qs = Order.objects.filter(date__year=datetime.now().year).count()
                return Response({'Number of orders this year': qs})
            elif type == 'week':
                TODAY = date.today()
                start = TODAY - timedelta(days=TODAY.weekday())
                end = start + timedelta(days=6)
                qs = Order.objects.filter(date__range=(start, end)).count()
                return Response({'Number of order this week': qs})
            else:
                return Response({})
        except Exception as e:
            return Response({'error':str(e)})