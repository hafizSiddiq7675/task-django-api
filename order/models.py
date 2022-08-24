from django.db import models



class Service(models.Model):
    name = models.CharField("name",max_length=255)

    def __str__(self):
        return str(self.id)
    
    
class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    
class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=True)