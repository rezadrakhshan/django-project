from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import make_password
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"credentials are invalid")
            return redirect("member:login")
    else:
        return render(request,"login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username has been taken")
            return redirect("member:register")
        if password==password2 and len(password) >= 4:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken")
                return redirect("member:register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("member:register")
            else:
                user = User.objects.create(username=username,email=email,password=make_password(password))
                user.save()
                auth.login(request,user)
                return redirect("shop:home")
        else:
                messages.info(request,"passwords are not the same")
                return redirect("member:register")
    else:
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect("member:login")