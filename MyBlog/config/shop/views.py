from django.shortcuts import render
from .models import Products, Order
from member.models import Profile
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def products(request):
    product = Products.objects.filter(availble=True)
    context = {"products": product}
    return render(request, "shop/products.html", context)


def add_procurement(request, id):
    product = Products.objects.get(id=id)
    user = Profile.objects.get(user=request.user)
    if user.amount <= product.price_with_discount():
        user.amount -= product.price_with_discount()
        user.save()
        order = Order.objects.create(user=user, product=product, status="P")
        messages.success(request,"سفارش شما با موفقیت ثبت شد")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        messages.error(request,"اعتبار شما برای ثبت سفارش کافی نیست لطفا حساب خود را شارژ کنید")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
def cart(request):
    user = Profile.objects.get(user=request.user)
    item = Order.objects.filter(user=user)
    context = {
        "items":item
    }
    return render(request,"shop/cart.html",context)


