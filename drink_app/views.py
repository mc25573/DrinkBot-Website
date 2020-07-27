from django.shortcuts import render
from .models import Drink, Ingredient, Pump, Extra
from django.db.models import Q
from .forms import MakeDrinkForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .cocktailLib import cocktailLib as clib

def home(request):
                                   
    form = MakeDrinkForm()
    
    ingrs = list(Ingredient.objects.values_list('name', flat=True))
    
    ingrs = dict.fromkeys(ingrs, (False,'')) # sets all ingrs to false
    
    extras = list(Extra.objects.values_list('name', flat=True))

    ingrs_avail = extras  
    pump_ingrs = []
    pumps = {}
    
    # create pump dictionary
    for i in Pump.objects.all():
        pumps[i.ingredient] = i.name
    
    for ingr in pumps:
        ingrs_avail.append(ingr)
        pump_ingrs.append(ingr)
       
    ingrs_avail = clib.soft_search(pumps,extras,ingrs_avail,ingrs)
    
    for ingr in list(ingrs_avail):
        if not ingrs_avail[ingr][0]:
           del ingrs_avail[ingr]
           
    ingrs_avail['None'] = (True,'None')
    
    # grab drinks that are shaken, stirred, blended, a shot, or tea
    drinks = Drink.objects.filter(Q(mix_type__exact='shaken')|Q(mix_type__exact='stirred')|
                                  Q(mix_type__exact='shot')|Q(mix_type__exact='tea')|
                                  Q(mix_type__exact='blended'))   
    
    # narrow down drinks further by ingredient available
    drinks = drinks.filter(ingredient1__in=ingrs_avail).filter(ingredient2__in=ingrs_avail
                  ).filter(ingredient3__in=ingrs_avail).filter(ingredient4__in=ingrs_avail
                  ).filter(ingredient5__in=ingrs_avail).filter(ingredient6__in=ingrs_avail
                  ).filter(ingredient7__in=ingrs_avail).filter(ingredient8__in=ingrs_avail
                  ).filter(non_pump_ingr1__in=ingrs_avail).filter(non_pump_ingr2__in=ingrs_avail
                  ).filter(non_pump_ingr3__in=ingrs_avail).order_by('name')
   
    # make more efficient!                                                              
    for drink in drinks:
        
        if drink.ingredient1 != ingrs_avail[drink.ingredient1][1]:
            drink.substitute1 = ingrs_avail[drink.ingredient1][1]
            drink.save()
        else:
            drink.substitute1 = 'None'
            drink.save()            
        if drink.ingredient2 != ingrs_avail[drink.ingredient2][1]:
            drink.substitute2 = ingrs_avail[drink.ingredient2][1]
            drink.save()
        else:
            drink.substitute2 = 'None'
            drink.save()
        if drink.ingredient3 != ingrs_avail[drink.ingredient3][1]:
            drink.substitute3 = ingrs_avail[drink.ingredient3][1]
            drink.save()
        else:
            drink.substitute3 = 'None'
            drink.save()   
            
        if drink.ingredient4 != ingrs_avail[drink.ingredient4][1]:
            drink.substitute4 = ingrs_avail[drink.ingredient4][1]
            drink.save()
        else:
            drink.substitute4 = 'None'
            drink.save()    
            
        if drink.ingredient5 != ingrs_avail[drink.ingredient5][1]:
            drink.substitute5 = ingrs_avail[drink.ingredient5][1]
            drink.save()
        else:
            drink.substitute5 = 'None'
            drink.save()   
            
        if drink.ingredient6 != ingrs_avail[drink.ingredient6][1]:
            drink.substitute6 = ingrs_avail[drink.ingredient6][1]
            drink.save()
        else:
            drink.substitute6 = 'None'
            drink.save()
            
        if drink.ingredient7 != ingrs_avail[drink.ingredient7][1]:
            drink.substitute7 = ingrs_avail[drink.ingredient7][1]
            drink.save()
        else:
            drink.substitute7 = 'None'
            drink.save() 
            
        if drink.ingredient8 != ingrs_avail[drink.ingredient8][1]:
            drink.substitute8 = ingrs_avail[drink.ingredient8][1]
            drink.save()
        else:
            drink.substitute8 = 'None'
            drink.save()  
    
    # the key is what is used in templates 
    context = {
        'drinks': drinks,
        'loops': range(1,9),
        'make_drink_form': form         
        }
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MakeDrinkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            choice = [form.cleaned_data['drink_size'],form.cleaned_data['hidden_field']]
            print(choice)
            messages.success(request, f'"{choice[1]}" Sent to Barbot')
            return HttpResponseRedirect(reverse('drinks-home')) # necessary to avoid form resubmit
    
    return render(request,'drink_app/home.html', context)















