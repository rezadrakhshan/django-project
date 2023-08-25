from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from .models import *
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 and len(password) >= 4:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username has been taken")
                return redirect("member:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email has been taken")
                return redirect("member:register")

            else:
                user_object = User.objects.create(username=username,email=email,password=make_password(password))
                user_object.save()
                user = User.objects.get(username=username)
                user_profile = Profile.objects.create(user=user)
                user_profile.save()
                auth.login(request,user)
                return redirect("member:profile")
        else:
            messages.info(request,"password error")
            return redirect("member:register")

    else:
        return render(request,"member/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("member:login")
    return render(request,"member/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method=="POST":
        profile.image = request.FILES.get("image")
        profile.address = request.POST["address"]
        profile.bio = request.POST['bio']
        profile.save()
    context = {
        "profile":profile
    }
    return render(request,"member/profile.html",context)