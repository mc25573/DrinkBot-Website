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
    
    # use substitution search to find available ingredients
    ingrs_avail = clib.soft_search(pumps,extras,ingrs_avail,ingrs)
    
    # remove unavailable ingrs
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
   
    # add ingredient substitutions for each available drink   
    for ingrs in drinks.values("ingredient1","ingredient2","ingredient3","ingredient4","ingredient5","ingredient6","ingredient7","ingredient8","name"):
        substitutes = []
        for i in range(8):            
            if ingrs['ingredient'+str(i+1)] != ingrs_avail[ingrs['ingredient'+str(i+1)]][1]:
                substitutes.append(ingrs_avail[ingrs['ingredient'+str(i+1)]][1])
            else:
                substitutes.append('None')
                
        Drink.objects.filter(name=ingrs['name']).update(substitute1=substitutes[0],substitute2=substitutes[1],
                                                        substitute3=substitutes[2],substitute4=substitutes[3],
                                                        substitute5=substitutes[4],substitute6=substitutes[5],
                                                        substitute7=substitutes[6],substitute8=substitutes[7])                                                 
   
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
            #print(Drink.objects.filter(name=choice[1]).values()[0])
            print(choice)
            messages.success(request, f'"{choice[1]}" Sent to Barbot')
            return HttpResponseRedirect(reverse('drinks-home')) # necessary to avoid form resubmit
    
    return render(request,'drink_app/home.html', context)















