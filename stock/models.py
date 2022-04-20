from unittest.util import _MAX_LENGTH
from django.db import models



# Create your models here.
class stock(models.Model):
    ticker = models.CharField(max_length=10)
    
    def __str__(self):
        return self.ticker
    
# create the stock component 
class data(models.Model):
    open = models.DecimalField(max_digits=10, decimal_places=3)
    close = models.DecimalField(max_digits=10, decimal_places=3)
    low = models.DecimalField(max_digits=10, decimal_places=3)
    high = models.DecimalField(max_digits=10, decimal_places=3)   
    
