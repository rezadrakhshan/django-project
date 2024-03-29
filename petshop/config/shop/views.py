from django.shortcuts import render
from .models import Team, Testimonial, Contact
from product.models import *
from blog.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="member:login")
def home(request):
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    product = Products.objects.filter(is_avable=True)
    blog = Blog.objects.filter(publish=True)[:2]
    context = {
        "teams": team,
        "testimoniales": testimonial,
        "products": product,
        "blogs": blog,
    }
    return render(request, "index.html", context)

@login_required(login_url="login")
def about(request):
    team = Team.objects.all()
    context = {"teams": team}
    return render(request, "about.html", context)

@login_required(login_url="login")
def service(request):
    testimonial = Testimonial.objects.all()
    context = {"testimoniales": testimonial}
    return render(request, "service.html", context)

@login_required(login_url="login")
def testimonial(request):
    testimonial = Testimonial.objects.all()
    context = {"testimoniales": testimonial}
    return render(request, "testimonial.html", context)

@login_required(login_url="login")
def team(request):
    team = Team.objects.all()
    context = {"teams": team}
    return render(request, "team.html", context)

@login_required(login_url="login")
def price(request):
    team = Team.objects.all()
    context = {"teams": team}
    return render(request, "price.html", context)

@login_required(login_url="login")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get("subject")
        text = request.POST.get("text")
        item = Contact.objects.create(
            name=name, email=email, subject=subject, message=text
        )
    return render(request, "contact.html")
