from django.db import models
from ingredients.models import Ingredient

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    price = models.FloatField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    # ingredients = models.ManyToManyField(Ingredient)

    def getName(self):
        return f"{self.name}"
    
    def getDesc(self):
        return f"{self.description}"

    def getPrice(self):
        return f"{self.price}"

    def __str__(self):
        return f"{self.pk}: {self.name} - {self.price}, {self.description} created at: {self.created_at}"

class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.FloatField()