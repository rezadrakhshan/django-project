from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from member.models import Profile
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
# Create your views here.

@login_required(login_url="member:login")
def comment(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message=  request.POST['message']
        profile = Profile.objects.get(user = request.user)
        comment = Comment.objects.create(user=profile, name=name, email=email, subject=subject,text=message,image=profile.image)
        messages.info(request,"Comment sent")
        return redirect("home:home")
    else:
        messages.info(request,"Error,Pleas Try Again")
    
    context = {
        "profile":request.user
    }
    return render(request,"comment.html",context)

def allcomment(request):
    comment = Comment.objects.filter(checked = True)
    context = {
        "comment":comment,
        "lencomment":len(comment)
    }
    return render(request,"testimonial.html",context)
    
        
