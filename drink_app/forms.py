# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:15:19 2020

@author: Matthew
"""

from django import forms

class MakeDrinkForm(forms.Form):
    DRINK_SIZE_CHOICES = [
    ('std', 'Standard'),
    ('sm', 'Small (4 oz)'),
    ('md', 'Medium (7 oz)'),
    ('lg', 'Large (10 oz)'),
    ]
    
    drink_size = forms.ChoiceField(choices=DRINK_SIZE_CHOICES)