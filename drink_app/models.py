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
    substitute1 = models.CharField(max_length=100,default='None')
    substitute2 = models.CharField(max_length=100,default='None')
    substitute3 = models.CharField(max_length=100,default='None')
    substitute4 = models.CharField(max_length=100,default='None')
    substitute5 = models.CharField(max_length=100,default='None')
    substitute6 = models.CharField(max_length=100,default='None')
    substitute7 = models.CharField(max_length=100,default='None')
    substitute8 = models.CharField(max_length=100,default='None')
    
    def get_ingrs(self):
        all_ingr = [self.ingredient1,self.ingredient2,self.ingredient3,self.ingredient4,self.ingredient5,self.ingredient6,
                self.ingredient7,self.ingredient8,self.non_pump_ingr1,self.non_pump_ingr2,self.non_pump_ingr3]
        ingredients = []       
        for ingr in all_ingr:
            if ingr != 'None':
                ingredients.append(ingr)              
        return ingredients
    
    def get_meas(self):
        all_meas = [self.measure1,self.measure2,self.measure3,self.measure4,self.measure5,self.measure6,
                self.measure7,self.measure8,self.non_pump_meas1,self.non_pump_meas2,self.non_pump_meas3]
        measures = []       
        for meas in all_meas:
            if meas != 'None':
                measures.append(meas)       
        return measures
    
    def get_subs(self):
        all_subs = [self.substitute1,self.substitute2,self.substitute3,self.substitute4,self.substitute5,self.substitute6,
                self.substitute7,self.substitute8,None,None,None]
        substitutes = []       
        for sub in all_subs:
            if sub != 'None':
                substitutes.append(sub)       
        return substitutes
    
    def get_ingrs_subs(self):
        all_ingr = [self.ingredient1,self.ingredient2,self.ingredient3,self.ingredient4,self.ingredient5,self.ingredient6,
                self.ingredient7,self.ingredient8,self.non_pump_ingr1,self.non_pump_ingr2,self.non_pump_ingr3]
        all_subs = [self.substitute1,self.substitute2,self.substitute3,self.substitute4,self.substitute5,self.substitute6,
                self.substitute7,self.substitute8,'None','None','None']       
        ingrs_subs = []       
        for ingr,sub in zip(all_ingr,all_subs):
            if ingr != 'None':
                ingrs_subs.append((ingr,sub))              
        return ingrs_subs
    
    def __str__(self):
        return self.name
    
    
class Pump(models.Model):
    name = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
   
    
class Extra(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name