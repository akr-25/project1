from django.shortcuts import render
from .models import Items 

def home(request):
    return render(request, 'stuff/home.html')

def suits(request):
    
    return render(request, 'stuff/suits.html', {'title': 'Suits'})