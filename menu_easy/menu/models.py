from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)
    #priority = models.TimeField()
    
class Tienda(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField()
    sloga = models.CharField(max_length = 400)
    
class Product(models.Model):
    title = models.CharField(max_length = 50)
    price = models.DecimalField(decimal_places = 3, max_digits = 6)
    description = models.TextField()
    service_init = models.TimeField()
    servece_end = models.TimeField()
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f'{self.title}'