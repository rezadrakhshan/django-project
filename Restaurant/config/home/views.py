from django.shortcuts import render
from .models import *
from comment.models import *
from reserve.models import *
# Create your views here.

def home(request):
    chef = Chefs.objects.all()[:4]
    comment = Comment.objects.filter(checked=True)[:4]
    time = Table.objects.all()
    context = {
        "chef":chef,
        "comment":comment,
        "time":time,
        "lentime":len(time),
        "lenchef":len(chef),
        "lencomment":len(comment),
    }
    return render(request,"index.html",context)

def about(request):
    chef = Chefs.objects.all()
    context = {
        "chef":chef,
        "lenchef":len(chef)
    }
    return render(request,"about.html",context)

def service(request):
    context = {
        
    }
    return render(request,"service.html",context)

def chefs(request):
    chef = Chefs.objects.all()
    context = {
        "chef":chef,
        "lenchef":len(chef)
    }
    return render(request,"team.html",context)
    

def error(request):
    return render(request,"404.html",status=500)