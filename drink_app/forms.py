# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:15:19 2020

@author: Matthew
"""

from django import forms
from .models import Pump

class MakeDrinkForm(forms.Form):
    
    DRINK_SIZE_CHOICES = [
    ('std', 'Standard'),
    ('3', 'Small (3 oz)'),
    ('5', 'Medium (5 oz)'),
    ('7', 'Large (7 oz)'),
    ]
    
    drink_size = forms.ChoiceField(choices=DRINK_SIZE_CHOICES)   
    hidden_field = forms.CharField(widget=forms.HiddenInput()) # for drink name
    
    def __init__(self, *args, **kwargs):
        super(MakeDrinkForm, self).__init__(*args, **kwargs)
        self.fields['drink_size'].label = "Choose Drink Size"
        self.label_suffix = ""  # Removes : as label suffix
        
        
class MakeYourOwn(forms.Form):
    
    total = forms.FloatField(label='Total Vol.',
                             initial=0,
                             max_value=8,
                             min_value=1,
                             #disabled=True,
                             widget=forms.NumberInput(attrs={'style': 'max-width:70px;','class':'total_field form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(MakeYourOwn, self).__init__(*args, **kwargs)
        for i, q in enumerate(Pump.objects.all()):
            self.fields[f"field_{i}_{q}"] = forms.FloatField(label=q.ingredient.title(),
                                                           initial=0,
                                                           max_value=8,
                                                           min_value=0,
                                                           widget=forms.NumberInput(attrs={'style': 'max-width:60px;','class': 'field_to_sum form-control'}))
        self.fields['total'].widget.attrs['readonly'] = True