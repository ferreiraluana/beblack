from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='Unknown')
    vendor = models.CharField(max_length=50, default='Unknown')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    imageUrl = models.CharField(max_length=50, default='')

    def __str__(self):
         return self.name

class CartProduct(models.Model):
    name = models.CharField(max_length=50, default='Unknown')
    vendor = models.CharField(max_length=50, default='Unknown')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    imageUrl = models.CharField(max_length=50, default='')
    customer = models.ForeignKey(get_user_model(), related_name='customer_product', on_delete=models.CASCADE, default=1)

    def __str__(self):
         return self.name