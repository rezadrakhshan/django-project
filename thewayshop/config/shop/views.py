from django.shortcuts import render, redirect
from .models import Product, WishList,Category
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

@login_required
def category(request, slug):
    cat = Category.objects.get(slug=slug)
    item = Product.objects.filter(category=cat)
    categories = Category.objects.filter(parent__isnull=True)
    category_product_count = {}

    def get_product_count(category):
        count = Product.objects.filter(category=category).count()
        for child in category.children.all():
            count += get_product_count(child)
        return count

    def populate_product_count(category):
        category_product_count[category.id] = get_product_count(category)
        for child in category.children.all():
            populate_product_count(child)

    for category in categories:
        populate_product_count(category)

    context = {
        "category": cat,
        "items": item,
        'categories': categories,
        'category_product_count': category_product_count,
    }
    return render(request, "shop.html", context)


    