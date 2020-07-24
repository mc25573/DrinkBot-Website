from django.shortcuts import render

def home(request):
    return render(request,'drink_app/home.html')
