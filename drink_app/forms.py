# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:15:19 2020

@author: Matthew
"""

from django import forms

class MakeDrinkForm(forms.Form):
    
    DRINK_SIZE_CHOICES = [
    ('std', 'Standard'),
    ('4', 'Small (4 oz)'),
    ('7', 'Medium (7 oz)'),
    ('10', 'Large (10 oz)'),
    ]
    
    drink_size = forms.ChoiceField(choices=DRINK_SIZE_CHOICES)   
    hidden_field = forms.CharField(widget=forms.HiddenInput()) # for drink name
    
    def __init__(self, *args, **kwargs):
        super(MakeDrinkForm, self).__init__(*args, **kwargs)
        self.fields['drink_size'].label = "Choose Drink Size"
        self.label_suffix = ""  # Removes : as label suffix