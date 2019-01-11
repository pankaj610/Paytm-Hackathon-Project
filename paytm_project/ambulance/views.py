from django.shortcuts import render
from . import models
# Create your views here.
def show_ambulance(request):
    
    return render(request, "index.html",{'ambulances':ambulances})
