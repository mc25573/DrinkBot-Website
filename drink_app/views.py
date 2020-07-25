from django.shortcuts import render
from .models import Drink
from django.db.models import Q
from .forms import MakeDrinkForm

def home(request):
    
    drinks = Drink.objects.filter(mix_type__exact='shaken'
                                 ).filter(glass__exact='Highball glass'
                                 ).order_by('name')
    #Q(mix_type__exact='shaken')|Q(mix_type__exact='stirred')|Q(mix_type__exact='shot')|Q(mix_type__exact='tea')
    
    form = MakeDrinkForm()
    
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
            choice = form.cleaned_data['']
    
    return render(request,'drink_app/home.html',context)
