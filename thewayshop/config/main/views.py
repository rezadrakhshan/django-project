from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team,Service


# home page function
@login_required
def home(request):
    return render(request, "index.html")


# about us page function
@login_required
def about(request):
    member = Team.objects.all()
    service = Service.objects.all()[:3]
    context = {
        "members": member,
        "services":service,
    }
    return render(request, "about.html", context)


@login_required
def service(request):
    member = Team.objects.all()
    service = Service.objects.all()
    context = {
        "members": member,
        "services":service
    }
    return render(request, "service.html", context)
