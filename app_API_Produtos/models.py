from django.db import models
from django.core.validators import MinValueValidator

# Define os campos da tabela Product
class Product(models.Model):
    
    product_name = models.CharField(max_length=100, unique=True, default='')
    product_description = models.CharField(max_length=500, blank=True, null=True, default='')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='')
    product_stock = models.PositiveIntegerField(default='')

    def __str__(self):
        return self.product_name