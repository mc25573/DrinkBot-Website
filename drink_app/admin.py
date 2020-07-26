from django.contrib import admin

# Register your models here.
from .models import Drink, Pump, Extra, Ingredient

admin.site.register(Drink)
admin.site.register(Pump)
admin.site.register(Extra)
admin.site.register(Ingredient)