from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from blog.models import Blog, Category, BlogComment
from member.models import Profile, SuperAccount, FollowersCount
from shop.models import Products,Order
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def is_super(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            pass
        else:
            return render(request, "404.html", status=404)
        return view_func(request, *args, **kwargs)

    return wrapper


@is_super
@login_required
def blog_list(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 99)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # All
    published = Blog.objects.filter(is_published=True)
    paginator_published = Paginator(published, 99)
    page_number_published = request.GET.get("page")
    page_obj_published = paginator_published.get_page(page_number_published)
    # Published
    draft = Blog.objects.filter(is_published=False)
    paginator_draft = Paginator(draft, 99)
    page_number_draft = request.GET.get("page")
    page_obj_draft = paginator_draft.get_page(page_number_draft)
    context = {
        "blogs": page_obj,
        "publisheds": page_obj_published,
        "drafts": page_obj_draft,
    }

    return render(request, "registration/dashboard/blog_list.html", context)


def blog_add(request):
    category = Category.objects.all()
    user = Profile.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        user = request.POST.get("author")
        tags = request.POST.getlist("tags")
        text = request.POST.get("text")
        cat = Category.objects.get(id=category)
        profile = Profile.objects.get(id=user)
        if title.strip() == "" or text.strip() == "":
            messages.error(request, "لطفا تمام مقادیر لازم را وارد کنید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            object = Blog.objects.create(
                title=title, category=cat, text=text, author=profile
            )
            object.tags.set(tags)
            messages.success(
                request, "مقاله با موفقیت ساخته شد پس از تایید ادمین ها منتشر میشود"
            )
            return redirect("dashboard:blog_list")
    context = {"categories": category, "users": user}
    return render(request, "registration/dashboard/add_blog.html", context)


@is_super
@login_required
def blog_edit(request, id):
    blog = Blog.objects.get(id=id)
    category = Category.objects.all()
    user = Profile.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        author = request.POST.get("author")
        tags = request.POST.getlist("tags")
        text = request.POST.get("text")
        slug = request.POST.get("slug")
        is_published = request.POST.get("is_published")
        cat = Category.objects.get(id=category)
        auth = Profile.objects.get(id=author)
        if title.strip() == "" or text.strip() == "":
            messages.error(request, "لطفا تمام مقادیر لازم را وارد کنید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            if is_published == "on":
                blog.title = title
                blog.author = auth
                blog.category = cat
                blog.tags.set(tags)
                blog.text = text
                blog.slug = slug
                blog.is_published = True
                blog.save()
                messages.success(request, "تغییرات با موفقیت اعمال گردید")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                blog.title = title
                blog.author = auth
                blog.category = cat
                blog.tags.set(tags)
                blog.text = text
                blog.slug = slug
                blog.is_published = False
                blog.save()
                messages.success(request, "تغییرات با موفقیت اعمال گردید")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    context = {"blog": blog, "categories": category, "users": user}
    return render(request, "registration/dashboard/edit.html", context)


@is_super
@login_required
def blog_remove(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("dashboard:blog_list")


@is_super
@login_required
def category(request):
    item = Category.objects.all()
    paginator = Paginator(item, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        title = request.POST.get("title")
        if Category.objects.filter(title=title).exists():
            messages.error(request, "این دسته بندی وجود دارد")
        else:
            messages.success(request, "دسته بندی با موفقیت ساخته شد")
    context = {"categories": page_obj}
    return render(request, "registration/dashboard/category.html", context)


@is_super
@login_required
def category_remove(request, id):
    if Category.objects.filter(id=id).exists():
        item = Category.objects.get(id=id)
        item.delete()
        messages.success(request, "دسته بندی با موفقیت حذف شد")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        messages.error(request, "دسته بندی با این آیدی وجود ندارد")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@is_super
@login_required
def blog_comment(request):
    comment = BlogComment.objects.all()
    paginator = Paginator(comment, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"comments": page_obj}
    return render(request, "registration/dashboard/comment.html", context)


@is_super
@login_required
def blog_comment_remove(request, id):
    item = BlogComment.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@is_super
@login_required
def super_user(request):
    # start user
    user = SuperAccount.objects.all()
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # end user
    # start gold
    gold = SuperAccount.objects.filter(super_account="G")
    paginator_gold = Paginator(gold, 10)
    page_number_gold = request.GET.get("page")
    page_obj_gold = paginator_gold.get_page(page_number_gold)
    # end gold
    # start silver
    silver = SuperAccount.objects.filter(super_account="S")
    paginator_silver = Paginator(silver, 10)
    page_number_silver = request.GET.get("page")
    page_obj_silver = paginator_silver.get_page(page_number_silver)
    # end silver
    # start last section
    d = SuperAccount.objects.filter(super_account="D")
    paginator_d = Paginator(d, 10)
    page_number_d = request.GET.get("page")
    page_obj_d = paginator_d.get_page(page_number_d)
    # end last section
    context = {
        "users": page_obj,
        "gold": page_obj_gold,
        "silver": page_obj_silver,
        "d": page_obj_d,
    }
    return render(request, "registration/dashboard/super_user.html", context)


@is_super
@login_required
def super_user_edit(request, id):
    user = SuperAccount.objects.get(slug=id)
    profile = Profile.objects.all()
    if request.method == "POST":
        user_profile = request.POST.get("profile")
        account = request.POST.get("account")
        slug = request.POST.get("slug")
        new_user = Profile.objects.get(id=user_profile)
        if slug.strip() == "":
            messages.error(request, "لطفا تمامی مقادیر را وارد کنید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        else:
            user.user = new_user
            user.super_account = account
            user.slug = slug
            user.save()
            messages.success(request, "تغییرات با موفقیت ثبت گردید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    context = {"user": user, "profile": profile}
    return render(request, "registration/dashboard/super_user_edit.html", context)


@is_super
@login_required
def super_user_remove(request, id):
    if SuperAccount.objects.filter(slug=id).exists():
        item = SuperAccount.objects.get(slug=id)
        item.delete()
        messages.success(request, "حساب با موفقیت حذف شد")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        messages.error(request, "حساب با این آیدی وجود ندارد")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@is_super
@login_required
def user_list(request):
    user = Profile.objects.all()
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"users": page_obj}
    return render(request, "registration/dashboard/user_list.html", context)


@is_super
@login_required
def user_edit(request, id):
    user = Profile.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        amount = request.POST.get("amount")
        is_superuser = request.POST.get("is_superuser")
        if (
            first_name.strip() == ""
            or last_name.strip() == ""
            or user_name.strip() == ""
            or email.strip() == ""
            or address.strip() == ""
            or amount.strip() == ""
        ):
            messages.error(request, "لطفا فضاهای خالی را از بین ببرید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            user.first_name = first_name
            user.last_name = last_name
            user.user_name = user_name
            user.email = email
            user.address = address
            user.amount = float(amount)
            if is_superuser == "on":
                admin = User.objects.get(id=user.user.id)
                admin.is_staff = True
                admin.save()
            else:
                admin = User.objects.get(id=user.user.id)
                admin.is_staff = False
                admin.save()
            user.save()
            messages.success(request, "تغییرات با موفقیت اعمال شد")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@is_super
@login_required
def user_remove(request, id):
    try:
        if request.user.is_superuser:
            item = Profile.objects.get(id=id)
            item.delete()
            messages.success(request, "کاربر با موفقیت حذف شد")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    except:
        messages.error(request, "عملیات انجام نشد!!!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@is_super
@login_required
def user_follower(request):
    try:
        follower_list = FollowersCount.objects.all()
        paginator = Paginator(follower_list, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"list": page_obj}
        return render(request, "registration/dashboard/follower_list.html", context)
    except:
        return render(request, "404.html", status=404)


@is_super
@login_required
def product_list(request):
    try:
        product = Products.objects.all()
        paginator = Paginator(product, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"products": page_obj}
        return render(request, "registration/dashboard/products_list.html", context)
    except:
        return render(request, "404.html", status=404)


@is_super
@login_required
def product_edit(request, id):
    try:
        item = Products.objects.get(id=id)
        if request.method == "POST":
            if request.FILES.get("image") == None:
                title = request.POST.get("title")
                description = request.POST.get("description")
                author = request.POST.get("author")
                page_count = request.POST.get("page_count")
                publication_date = request.POST.get("publication_date")
                book_cover = request.POST.get("book_cover")
                tag = request.POST.get("tag")
                price = request.POST.get("price")
                discount = request.POST.get("discount")
                availble = request.POST.get("availble")
                if (
                    title.strip() == ""
                    or description.strip() == ""
                    or author.strip() == ""
                    or page_count.strip() == ""
                    or publication_date.strip() == ""
                    or book_cover.strip() == ""
                    or price.strip() == ""
                    or discount.strip() == ""
                ):
                    messages.error(request, "لطفا تمام مقادیر را وارد کنید")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
                else:
                    item.title = title
                    item.description = description
                    item.author = author
                    item.page_count = int(page_count)
                    item.publication_date = publication_date
                    item.book_cover = book_cover
                    item.tag = tag
                    item.price = float(price)
                    item.discount = float(discount)
                    if availble == "on":
                        item.availble = True
                    else:
                        item.availble = False
                    item.save()
                    messages.success(request, "تغییرات با موفقیت اعمال گردید")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            elif request.FILES.get("image") != None:
                title = request.POST.get("title")
                description = request.POST.get("description")
                author = request.POST.get("author")
                image = request.FILES.get("image")
                page_count = request.POST.get("page_count")
                publication_date = request.POST.get("publication_date")
                book_cover = request.POST.get("book_cover")
                tag = request.POST.get("tag")
                price = request.POST.get("price")
                discount = request.POST.get("discount")
                availble = request.POST.get("availble")
                if (
                    title.strip() == ""
                    or description.strip() == ""
                    or author.strip() == ""
                    or page_count.strip() == ""
                    or publication_date.strip() == ""
                    or book_cover.strip() == ""
                    or price.strip() == ""
                    or discount.strip() == ""
                ):
                    messages.error(request, "لطفا تمام مقادیر را وارد کنید")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
                else:
                    item.title = title
                    item.description = description
                    item.author = author
                    item.image = image
                    item.page_count = int(page_count)
                    item.publication_date = publication_date
                    item.book_cover = book_cover
                    item.tag = tag
                    item.price = float(price)
                    item.discount = float(discount)
                    if availble == "on":
                        item.availble = True
                    else:
                        item.availble = False
                    item.save()
                    messages.success(request, "تغییرات با موفقیت اعمال گردید")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        return render(
            request, "registration/dashboard/product_edit.html", {"item": item}
        )
    except:
        return render(request, "404.html", status=404)


@is_super
@login_required
def product_remove(request, id):
    try:
        item = Products.objects.get(id=id)
        item.delete()
        messages.success(request, "محصول با موفقیت حذف شد")
        return redirect("dashboard:product_list")
    except:
        return render(request, "404.html", status=404)

@is_super
@login_required
def add_product(request):
    try:
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            author = request.POST.get("author")
            image = request.FILES.get("image")
            page_count = request.POST.get("page_count")
            publication_date = request.POST.get("publication_date")
            book_cover = request.POST.get("book_cover")
            tag = request.POST.get("tag")
            price = request.POST.get("price")
            discount = request.POST.get("discount")
            availble = request.POST.get("availble")
            if (
                title.strip() == ""
                or description.strip() == ""
                or author.strip() == ""
                or page_count.strip() == ""
                or publication_date.strip() == ""
                or book_cover.strip() == ""
                or price.strip() == ""
                or discount.strip() == ""
            ):
                messages.error(request, "لطفا تمام مقادیر را وارد کنید")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                if availble == "on":
                    new = Products.objects.create(
                        title=title,
                        description=description,
                        author=author,
                        image=image,
                        page_count=int(page_count),
                        publication_date=publication_date,
                        book_cover=book_cover,
                        tag=tag,
                        price=float(price),
                        discount=float(discount),
                        availble=True,
                    )
                    messages.success(request, "محصول با موفقیت اضافه شد")
                    return redirect("dashboard:product_list")
                else:
                    new = Products.objects.create(
                        title=title,
                        description=description,
                        author=author,
                        image=image,
                        page_count=int(page_count),
                        publication_date=publication_date,
                        book_cover=book_cover,
                        tag=tag,
                        price=float(price),
                        discount=float(discount),
                        availble=False,
                    )
                    messages.success(request, "محصول با موفقیت اضافه شد")
                    return redirect("dashboard:product_list")
        return render(request, "registration/dashboard/add_product.html")
    except:
        return render(request, "404.html", status=404)

@is_super
@login_required
def order_list(request):
    try:
        order = Order.objects.all()
        paginator = Paginator(order, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request,"registration/dashboard/order_list.html",{"order":page_obj})
    except:
        return render(request, "404.html", status=404)
    
def order_edit(request,id):
    try:
        order = Order.objects.get(slug=id)
        if request.method == "POST":
            status = request.POST.get("status")
            slug = request.POST.get("slug")
            if slug.strip() == "":
                messages.error(request,"لطفا تمام مقادیر لازم را وارد کنید")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                order.status = status
                order.slug = slug
                order.save()
                messages.success(request,"تغییرات با موفقیت ثبت شد")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        return render(request,"registration/dashboard/order_edit.html",{"order":order})
    except:
        return render(request, "404.html", status=404)
        