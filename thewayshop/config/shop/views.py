from django.shortcuts import render,redirect
from .models import Product
# Create your views here.


def detail(request,id):
    if Product.objects.filter(id=id,avaible=True).exists():
        item = Product.objects.get(id=id)
        product = Product.objects.filter(category=item.category,avaible=True)
        context = {
            "item":item,
            "products":product
        }
        return render(request,"shop-detail.html",context)
    else:
        return redirect("main:home")

#5432