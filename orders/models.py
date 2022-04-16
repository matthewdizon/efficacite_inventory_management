from django.db import models
from ingredients.models import Ingredient
# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=250)

    def getstatus(self):
        return f"{self.status}"
    
    def __str__(self):
        return f"{self.pk}: {self.status}"


class Order(models.Model):
    ingredient_order = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.FloatField()
    ordered_at = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    payment_mode = models.CharField(max_length=4)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def getqty(self):
        return f"{self.qty}"
    
    def gettotal(self):
        return f"{self.total}"

    def getpayment_mode(self):
        return f"{self.payment_mode}"

    def __str__(self):
        return f"{self.pk}: {self.ingredient_order} - {self.qty}, {self.payment_mode}, {self.total} created at: {self.ordered_at}"

