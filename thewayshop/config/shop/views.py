from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, WishList, Category, Cart
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        if WishList.objects.filter(user=request.user, product=product).exists():
            wish = WishList.objects.filter(user=request.user, product=product)
            wish.delete()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            new_whish = WishList.objects.create(user=request.user, product=item)
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect("/")


@login_required
def removewish(request, pk):
    if WishList.objects.filter(slug=pk).exists():
        item = WishList.objects.filter(slug=pk)
        item.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect("/")


@login_required
def wishlist(request):
    item = WishList.objects.filter(user=request.user)
    context = {"items": item}
    return render(request, "wishlist.html", context)


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
        "categories": categories,
        "category_product_count": category_product_count,
    }
    return render(request, "shop.html", context)


@login_required
def filter_price(request):
    if request.method == "GET":
        amount = request.GET.get("amount")
        category = request.GET.get("category")
        parts = amount.split(" - ")
        start_price = int(parts[0].strip("$"))
        end_price = int(parts[1].strip("$"))
        cat = Category.objects.get(slug=category)
        item = Product.objects.filter(
            price__gte=start_price, price__lte=end_price, category=cat
        )
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
            "categories": categories,
            "category_product_count": category_product_count,
        }
        return render(request, "shop.html", context)
    else:
        return redirect("/")


@login_required
def search(request):
    if request.method == "GET":
        word = request.GET.get("search")
        category = request.GET.get("type")
        cat = Category.objects.get(slug=category)
        item = Product.objects.filter(title__icontains=word, avaible=True, category=cat)
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
            "categories": categories,
            "category_product_count": category_product_count,
        }
        return render(request, "shop.html", context)
    else:
        return redirect("/")


@login_required
def add_cart(request):
    if request.method == "POST":
        size = request.POST.get("size")
        count = request.POST.get("count")
        product = request.POST.get("product")
        item = Product.objects.get(id=product)
        if Cart.objects.filter(product=item, user=request.user, size=size).exists():
            cart = Cart.objects.get(product=item, user=request.user, size=size)
            cart.count = cart.count + int(count)
            cart.save()
            messages.success(request, "Your order has been registered")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            new_order = Cart.objects.create(
                user=request.user, product=item, size=size, count=count
            )
            messages.success(request, "Your order has been registered")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


# FIXME:
@login_required
def cart(request):
    items = Cart.objects.filter(user=request.user)
    if request.method == "POST":
        quantity = request.POST.get("count")
        slug = request.POST.get("slug")
        selected_cart = get_object_or_404(Cart, user=request.user, slug=slug)
        selected_cart.count = quantity
        selected_cart.save()
        messages.success(request, "The changes were made successfully")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    context = {"items": items}
    return render(request, "cart.html", context)


@login_required
def remove_cart(request, slug):
    item = get_object_or_404(Cart, user=request.user, slug=slug)
    item.delete()
    messages.success(request, "The order was successfully deleted")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
