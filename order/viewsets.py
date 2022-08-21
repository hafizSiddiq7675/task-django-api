
from .models import Order, OrderItem
from rest_framework.response import Response
import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@api_view(['GET', 'POST']) 
@csrf_exempt 
def create_order(request, *args, **kwargs): 
    if request.method == 'POST': 
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
         
    else: 
        # order = [(order.id,order.date) for order in Order.objects.all()]
        order_qs = Order.objects.all().values()
        orderitem_qs = OrderItem.objects.all().values() 
        return Response({"Order":order_qs,"OrderItem":orderitem_qs}) 

