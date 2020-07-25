from django.contrib import admin

# Register your models here.
from .models import Drink, Pump, Extra

admin.site.register(Drink)
admin.site.register(Pump)
admin.site.register(Extra)