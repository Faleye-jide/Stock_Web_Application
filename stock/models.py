from django.db import models
import joblib



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
    predicted_close = models.DecimalField(max_digits=7, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        model = joblib.load('ml_model/stock_model.pkl')
        model.predict([self.open, self.low, self.high])
        return super().save(*args, **kwargs)
    
