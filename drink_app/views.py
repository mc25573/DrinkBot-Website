from django.shortcuts import render
from .models import Drink
from django.db.models import Q

def home(request):
    
    drinks = Drink.objects.filter(mix_type__exact='shaken'
                                 ).filter(glass__exact='Highball glass'
                                 ).order_by('name')
    #Q(mix_type__exact='shaken')|Q(mix_type__exact='stirred')|Q(mix_type__exact='shot')|Q(mix_type__exact='tea')
    
    context = {
        'drinks': drinks, # the key is what is used in templates 
        'loops': range(1,9)          
        }
    
    return render(request,'drink_app/home.html',context)
