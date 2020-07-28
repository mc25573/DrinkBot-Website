from django.shortcuts import render
from .models import Drink, Ingredient, Pump, Extra
from django.db.models import Q
from .forms import MakeDrinkForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .cocktailLib import cocktailLib as clib
from django.utils.safestring import mark_safe

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
    pump_ingrs = clib.soft_search(pumps,extras,pump_ingrs,ingrs)
    
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
            drink_choice = Drink.objects.filter(name=choice[1]).values()[0]
            
            # make function for this code!
            volumes = []
            ingrs_used = []
            manual_ingrs = []
            np_ingrs = []
            np_meas = []
            np_vols = []
            ingrs_disp = []
            
            for i in range(3):
                if drink_choice['non_pump_ingr'+str(i+1)] != 'None':
                    np_ingrs.append(drink_choice['non_pump_ingr'+str(i+1)])
                    np_meas.append(drink_choice['non_pump_meas'+str(i+1)])
                else:
                    break                
            for i in range(8):  
                if drink_choice['measure'+str(i+1)] != 'None':
                    ingrs_used.append( (drink_choice['ingredient'+str(i+1)],i+1) )
                    volumes.append(float(drink_choice['measure'+str(i+1)].split(' ')[0]))        
                else:
                    break                
            try:                       
                choice[0] = int(choice[0])
            except: 
                choice[0] = sum(volumes)        
                        
            multiplier = choice[0]/sum(volumes)              
                               
            volumes = [round(x * multiplier,2) for x in volumes]
            
            for ingr,idx in ingrs_used:
                if not pump_ingrs[ingr][0]:
                    manual_ingrs.append((ingr,idx,ingrs_avail[ingr][1]))
                else:
                    ingrs_disp.append((ingr,idx,pump_ingrs[ingr][1]))
            
            for meas in np_meas:
                try:
                    np_vols.append(f"{float(meas.split(' ')[0]) * multiplier:.2g} {meas.partition(' ')[2]}")
                except:
                    np_vols.append(meas)
            
            sub_str = ''
            
            for ingr,idx,sub in manual_ingrs:
                if ingr == sub:
                    man_sub_str = ''
                else:
                    man_sub_str = f"({ingrs_avail[ingr][1].title()})"
                    
                sub_str += f"{volumes[idx-1]} oz {ingr.title()} {man_sub_str}<br/>"    
                        
            for meas,ingr in zip(np_vols,np_ingrs):
                sub_str += f"{meas} {ingr.title()}<br/>"
            
            # tell each pump how many oz to pump
            pump_disp = {}
            for i in range(len(pumps)):
                pump_disp['pump'+str(i)] = 0
                       
            for ingr,idx,sub in ingrs_disp:
                pump_disp[pumps[sub]] += volumes[idx-1]

            print(pump_disp)
            messages.success(request, mark_safe(f'"{choice[1]}" Sent to Barbot'))
            if sub_str != '':
                messages.success(request, mark_safe(f"<strong>You need to add</strong>:<br>{sub_str}"))
            return HttpResponseRedirect(reverse('drinks-home')) # necessary to avoid form resubmit
    
    return render(request,'drink_app/home.html', context)















