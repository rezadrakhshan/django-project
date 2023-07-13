from django.shortcuts import render
from .models import Post,Food,Breakfast,Lunch,Dinner
from django.core.paginator import Paginator
# Create your views here.

def homepage(request):
    return render(request,"index.html")

def postlist(request):
    post= Post.objects.filter(status="published")
    paginator = Paginator(post,3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    context = {
        'page_obj':page_obj,

    }
    return render(request,'listnews.html',context)

def order(request):
    foods = Food.objects.filter(status="Available")

    return render(request,"order.html",{'foods':foods})


def about(request):


    return render(request,"about.html")

def breakfast(request):
    breakfast = Breakfast.objects.filter(status="Available")

    return render(request,"breakfast.html",{'breakfast':breakfast})

def lunch(request):
    lunch = Lunch.objects.filter(status="Available")

    return render(request,"lunch.html",{'lunch':lunch})

def dinner(request):
    dinner = Dinner.objects.filter(status="Available")

    return render(request,"dinner.html",{'dinner':dinner})


def collectionbozorg(request):


    return render(request,"collection.html")


def booktabel(request):


    return render(request,"booktabel.html")
