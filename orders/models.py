from django.db import models
from ingredients.models import Ingredient
from django.utils.timezone import now

STATUS = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('served', 'Served'),
    )

PAYMENT_MODE = (
        ('cash', 'Cash'),
        ('card', 'Card'),
    )
class Order(models.Model):
    ordered_at = models.DateTimeField(default=now)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    payment_mode = models.CharField(max_length=4, choices=PAYMENT_MODE)
    status = models.CharField(max_length=20, choices=STATUS)
    
    def getstatus(self):
        return f"{self.status}"
    
    def gettotal(self):
        return f"{self.total}"

    def getpayment_mode(self):
        return f"{self.payment_mode}"

    def __str__(self):
        return f"{self.pk}: {self.payment_mode}, {self.status}, {self.total} created at: {self.ordered_at}"

class ItemOrder(models.Model):
   ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
   line_total = models.DecimalField(decimal_places=2, max_digits=25, default=0)
   quantity = models.IntegerField()
 
   def getIngredientID(self):
       return self.ingredient_id
 
   def getOrderID(self):
       return self.order_id

   def getQuantity(self):
       return self.quantity

   def getLineTotal(self):
       price = self.ingredient_id.get_price()
       return self.quantity * int(price)
 
   def __str__(self):
       return str(self.pk) + ": (Item ID) " + str(self.ingredient_id) + ", (Order ID) " + str(self.order_id) + ", (Quantity) " + str(self.quantity)