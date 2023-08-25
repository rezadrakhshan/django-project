from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.


def add(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        time = request.POST['time']
        people = request.POST['people']
        request = request.POST['request']
        tabletime = Table.objects.get(title=time)
        add = Reserve.objects.create(name=name, email=email, time=time, no_of_people=people, request=request)
        add.save()
        tabletime.delete()
        return redirect("home:home")
    else:
        return render(request,"index.html")