from django.db import models
from django.utils.translation import gettext_lazy as _

class Services(models.Model):
    class Meta:
        db_table = 'services'
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True) #, null=True)
    name = models.CharField("name",max_length=255)
    
    
class Orders(models.Model):

    class Meta:
        db_table = 'orders'
        
    date = models.DateField(_("date"), auto_now=False, auto_now_add=False)
    
    
class OrderItems(models.Model):
    
    class Meta:
        db_table = 'order_items'
        
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"))
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    
    
