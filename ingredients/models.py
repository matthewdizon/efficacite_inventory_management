from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pk}: {self.name} created at: {self.created_at}"