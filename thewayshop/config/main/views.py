from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team


# home page function
@login_required
def home(request):
    return render(request, "index.html")


# about us page function
@login_required
def about(request):
    member = Team.objects.all()
    context = {
        "members": member,
    }
    return render(request, "about.html", context)
