from django.contrib import admin
from .models import OrderItems, Orders, Services
# Register your models here.


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Orders)
class Orders(admin.ModelAdmin):
    list_display = ['id','date']

    
@admin.register(OrderItems)
class OrderItems(admin.ModelAdmin):
    list_display = ['id','order_id','service_id','quantity','price']