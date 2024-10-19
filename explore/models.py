from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.TextField(null = True, blank = True)
    category = models.TextField(null = True, blank = True)
    restaurant_name = models.TextField(null = True, blank = True)
    image = models.URLField(null = True, blank = True)
    city = models.TextField(null = True, blank = True)
    price = models.IntegerField(null = True, blank = True)
    rating = models.FloatField(null = True, blank = True)
    specialized = models.TextField(null = True, blank = True)
    takeaway = models.BooleanField(null = True, blank = True)
    delivery = models.BooleanField(null = True, blank = True)
    outdoor = models.BooleanField(null = True, blank = True)
    smoking_area = models.BooleanField(null = True, blank = True)
    wifi = models.BooleanField(null = True, blank = True)
