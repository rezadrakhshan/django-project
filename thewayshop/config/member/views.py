from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username.strip() == "" or password.strip() == "":
            messages.error(request, "pleas enter correct values")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")
        else:
            messages.error(request, "username or password is invalid")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    return render(request, "auth/login.html")


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        if email.strip() == "" or username.strip() == "" or password.strip() == "":
            messages.error(request, "pleas enter correct values")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        elif len(password) <= 4:
            messages.error(request, "pleas enter valid password")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username is taken")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                user = User.objects.create(
                    email=email, password=make_password(password), username=username
                )
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                return redirect("main:home")
    return render(request, "auth/register.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect("member:login")