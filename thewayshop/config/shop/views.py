from django.shortcuts import render, redirect
from .models import Product, WishList
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def detail(request, id):
    if Product.objects.filter(id=id, avaible=True).exists():
        item = Product.objects.get(id=id)
        product = Product.objects.filter(category=item.category, avaible=True)
        context = {"item": item, "products": product}
        return render(request, "shop-detail.html", context)
    else:
        return redirect("main:home")


@login_required
def wishitem(request, product):
    if Product.objects.filter(id=product).exists():
        item = Product.objects.get(id=product)
        if WishList.objects.filter(user=request.user,product=product).exists():
            wish = WishList.objects.filter(user=request.user,product=product)
            wish.delete()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            new_whish = WishList.objects.create(user=request.user, product=item)
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect("/")


@login_required
def removewish(request,pk):
    if WishList.objects.filter(slug=pk).exists():
        item = WishList.objects.filter(slug=pk)
        item.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect("/")



@login_required
def wishlist(request):
    item = WishList.objects.filter(user=request.user)
    context = {
        "items":item
    }
    return render(request,"wishlist.html",context)