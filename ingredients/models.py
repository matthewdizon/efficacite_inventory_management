from django.db import models
from suppliers.models import Supplier
from django.utils.timezone import now

METRIC_CHOICES = (
    ('kg','kilogram'),
    ('mg','milligram'),
    ('g','gram'),
)

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    current_quantity = models.FloatField(max_length=250)
    quantity_threshold = models.FloatField(max_length=250)
    metric = models.CharField(max_length=25, choices=METRIC_CHOICES, default='kg')
    expiration_date = models.DateTimeField(default=now)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=500)
    
    def __str__(self):
        return f"{self.pk}: {self.name}"

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.current_quantity

    def get_quantity_ratio(self):
        return self.current_quantity / self.quantity_threshold

 