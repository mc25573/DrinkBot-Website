from django.shortcuts import render
from .models import Drink, Ingredient
from django.db.models import Q
from .forms import MakeDrinkForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .cocktailLib import cocktailLib as clib

def home(request):
    
    '''drinks = Drink.objects.filter(mix_type__exact='shaken'
                                 ).filter(glass__exact='Highball glass'
                                 ).order_by('name')'''
    drinks = Drink.objects.filter(Q(mix_type__exact='shaken')|Q(mix_type__exact='stirred')|Q(mix_type__exact='shot')|Q(mix_type__exact='tea')|Q(mix_type__exact='blended'))
                                   
    form = MakeDrinkForm()
    
    ingrs = list(Ingredient.objects.values_list('name', flat=True))
    
    ingrs = dict.fromkeys(ingrs, (False,'')) # sets all ingrs to false
    
    # temp
    extras = ['lime','water','sugar','angostura bitters','dry vermouth','sprite','grenadine','mint leaves','club soda','powdered sugar','brown sugar',
          'cinnamon','egg','nutmeg','simple syrup','vanilla extract','worcestershire sauce','olive brine','lemon']

    ingrs_avail = extras  
    pump_ingrs = []
    
    # temp
    pumps = {'num_pumps': 5,
     'vodka': 'pump0',
     'white rum': 'pump1',
     'orange juice': 'pump2',
     'gin': 'pump3',
     'triple sec': 'pump4'}
    
    # temp
    for ingr in pumps:
        if ingr != 'num_pumps':
            ingrs_avail.append(ingr)
            pump_ingrs.append(ingr)
       
    ingrs_avail = clib.soft_search(pumps,extras,ingrs_avail,ingrs)
    
    for ingr in list(ingrs_avail):
        if not ingrs_avail[ingr][0]:
           del ingrs_avail[ingr]
           
    ingrs_avail['None'] = (True,'None')
           
    drinks = drinks.filter(ingredient1__in=ingrs_avail).filter(ingredient2__in=ingrs_avail
                  ).filter(ingredient3__in=ingrs_avail).filter(ingredient4__in=ingrs_avail
                  ).filter(ingredient5__in=ingrs_avail).filter(ingredient6__in=ingrs_avail
                  ).filter(ingredient7__in=ingrs_avail).filter(ingredient8__in=ingrs_avail
                  ).filter(non_pump_ingr1__in=ingrs_avail).filter(non_pump_ingr2__in=ingrs_avail
                  ).filter(non_pump_ingr3__in=ingrs_avail)
       
    
    context = {
        'drinks': drinks, # the key is what is used in templates 
        'loops': range(1,9) ,
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
