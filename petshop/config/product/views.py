from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def home(request):
    product = Products.objects.filter(is_avable=True)
    context = {"product": product}
    return render(request, "product.html", context)
