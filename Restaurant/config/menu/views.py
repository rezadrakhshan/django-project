from django.shortcuts import render
from .models import *
# Create your views here.

def menu(request):
    breakfast = Menu.objects.filter(category = "B")
    context = {
        "breakfast":breakfast
    }
    return render(request,"menu/menu.html",context)

def lunch(request):
    lunch = Menu.objects.filter(category = "L")
    context = {
        "lunch":lunch
    }
    return render(request,"menu/lunch.html",context)

def dinner(request):
    dinner = Menu.objects.filter(category = "D")
    context = {
        "dinner":dinner
    }
    return render(request,"menu/dinner.html",context)

