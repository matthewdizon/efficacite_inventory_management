from django.db import models
from suppliers.models import Supplier
from django.utils.timezone import now
from datetime import datetime, timezone

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

    def get_expiration_priority(self):
        d0 = datetime.now(timezone.utc)
        delta = self.expiration_date - d0
        return delta

class IngredientBatch(models.Model):
   ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   quantity = models.FloatField(max_length=250)
   expiration_date = models.DateTimeField(default=now)
   created_at = models.DateTimeField(default=now)
   
   def get_ingredient_id(self):
       return self.ingredient_id

   def __str__(self):
       return f"{self.pk}: {self.ingredient_id}"