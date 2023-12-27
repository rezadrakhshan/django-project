from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def step_one(request):
    try:
        user = Profile.objects.get(user=request.user)
        return redirect("movie:home")
    except:
        if request.method == "POST":
            f_name = request.POST.get("firstname")
            l_name = request.POST.get("lastname")
            country = request.POST.get("country")
            phone = request.POST.get("phone")

            profile = Profile.objects.create(
                user=request.user,
                first_name=f_name,
                last_name=l_name,
                country=country,
                phone_number=phone,
            )
            return redirect("member:step_two")
    return render(request,"profile.html")
@login_required
def step_two(request):
    if request.method == "POST":
        user = Profile.objects.get(user=request.user)
        user.user_name = request.POST.get("username")
        user.bio = request.POST.get('bio')
        user.adress = request.POST.get('adress')
        user.email = request.POST.get('email')
        user.image = request.FILES.get("image")
        user.save()
        return redirect("movie:home")
    return render(request,"profile_step2.html")


def update(request):
    user = Profile.objects.get(user=request.user)
    if request.method=="POST":
        user.first_name = request.POST.get("firstname")
        user.last_name = request.POST.get('lastname')
        user.country = request.POST.get('country')
        user.phone_number = request.POST.get("phone")
        user.user_name = request.POST.get("username")
        user.bio = request.POST.get('bio')
        user.adress = request.POST.get('adress')
        user.email = request.POST.get('email')
        if request.FILES.get('image') != None:
            user.image = request.FILES.get("image")
            user.save()
        else:
            user.save( )
    context = {
        "profile":user
    }
    return render(request,"update_profile.html",context)