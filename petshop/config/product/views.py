from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    product = Products.objects.filter(is_avable=True)
    context = {"product": product}
    return render(request, "product.html", context)
