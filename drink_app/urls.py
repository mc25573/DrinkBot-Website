# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 01:00:21 2020

@author: Matthew
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'drinks-home'),
    path('make-your-own/', views.make_your_own, name='drink-make-your-own')
]