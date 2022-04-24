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
    ingredient_order = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.FloatField()
    ordered_at = models.DateTimeField(default=now)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    payment_mode = models.CharField(max_length=4, choices=PAYMENT_MODE)
    status = models.CharField(max_length=20, choices=STATUS)

    def getqty(self):
        return f"{self.qty}"
    
    def getstatus(self):
        return f"{self.status}"
    
    def gettotal(self):
        return f"{self.total}"

    def getpayment_mode(self):
        return f"{self.payment_mode}"

    def __str__(self):
        return f"{self.pk}: {self.ingredient_order} - {self.qty}, {self.payment_mode}, {self.status}, {self.total} created at: {self.ordered_at}"

