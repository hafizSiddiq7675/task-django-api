from django.contrib import admin
from .models import OrderItem, Order, Service
# Register your models here.


@admin.register(Service)
class Services(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Order)
class Orders(admin.ModelAdmin):
    list_display = ['id','date']

    
@admin.register(OrderItem)
class OrderItems(admin.ModelAdmin):
    list_display = ['id','quantity','price','service_id','order_id']#,'service_id','order_id'