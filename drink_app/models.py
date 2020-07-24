from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_modified = models.CharField(max_length=100)
    drink_alternate = models.CharField(max_length=100)
    garnish1 = models.CharField(max_length=100)
    garnish2 = models.CharField(max_length=100)
    glass = models.CharField(max_length=100)
    iba = models.CharField(max_length=100)
    ingredient1 = models.CharField(max_length=100)
    ingredient2 = models.CharField(max_length=100)
    ingredient3 = models.CharField(max_length=100)
    ingredient4 = models.CharField(max_length=100)
    ingredient5 = models.CharField(max_length=100)
    ingredient6 = models.CharField(max_length=100)
    ingredient7 = models.CharField(max_length=100)
    ingredient8 = models.CharField(max_length=100)
    instructions = models.TextField()
    measure1 = models.CharField(max_length=100)
    measure2 = models.CharField(max_length=100)
    measure3 = models.CharField(max_length=100)
    measure4 = models.CharField(max_length=100)
    measure5 = models.CharField(max_length=100)
    measure6 = models.CharField(max_length=100)
    measure7 = models.CharField(max_length=100)
    measure8 = models.CharField(max_length=100)
    non_pump_ingr1 = models.CharField(max_length=100)
    non_pump_ingr2 = models.CharField(max_length=100)
    non_pump_ingr3 = models.CharField(max_length=100)
    non_pump_meas1 = models.CharField(max_length=100)
    non_pump_meas2 = models.CharField(max_length=100)
    non_pump_meas3 = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=300)
    mix_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Pump(models.Model):
    name = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name