from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from member.views import check_profile
from member.models import Profile,SuperAccount
from config.settings import COUNT_VIEWS
from django.db.models import F


# Create your views here.


@login_required
@check_profile
def addblog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        tags = request.POST.getlist("tags")
        text = request.POST.get("text")
        cat = Category.objects.get(id=category)
        user = Profile.objects.get(user=request.user)
        if title.strip() == "" or text.strip() == "":
            messages.error(request, "لطفا تمام مقادیر لازم را وارد کنید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            object = Blog.objects.create(
                title=title, category=cat, text=text, author=user
            )
            object.tags.set(tags)
            messages.success(
                request, "مقاله با موفقیت ساخته شد پس از تایید ادمین ها منتشر میشود"
            )
            return redirect("member:myblog")

    context = {"categories": Category.objects.all}
    return render(request, "blog/addblog.html", context)


@login_required
@check_profile
def removeblog(request, slug):
    item = Blog.objects.get(slug=slug)
    if item.author == request.user:
        item.delete()
        messages.info(request, "مقاله با موفقیت حذف شد")
    else:
        return render(request, "404.html", status=404)
    return redirect("member:myblog")


@login_required
@check_profile
def editblog(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = Profile.objects.get(user=request.user)
    if blog.is_published == True:
        return render(request, "404.html", status=404)
    else:
        if blog.author == user:
            if request.method == "POST":
                title = request.POST.get("title")
                category = request.POST.get("category")
                tags = request.POST.getlist("tags")
                text = request.POST.get("text")
                cat = Category.objects.get(id=category)
                if title.strip() == "" or text.strip() == "":
                    messages.error(request, "لطفا تمام مقادیر لازم را وارد کنید")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
                else:
                    blog.title = title
                    blog.category = cat
                    blog.tags.set(tags)
                    blog.text = text
                    blog.save()
                    messages.success(request, "تغییرات با موفقیت اعمال گردید")
                    return redirect("member:myblog")
        else:
            return render(request, "404.html", status=404)
        context = {"categories": Category.objects.all, "blog": blog}
        return render(request, "blog/addblog.html", context)


@login_required
@check_profile
def detail(request, slug):
    global COUNT_VIEWS
    object = Blog.objects.get(slug=slug)
    item = BlogComment.objects.filter(blog=object, parent__isnull=True)
    profile = Profile.objects.get(user=request.user)
    author = Blog.objects.filter(author=object.author, is_published=True)
    if request.method == "POST" and object.is_published == True:
        text = request.POST.get("text")
        comment = BlogComment.objects.create(user=profile, blog=object, text=text)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    ip_address = request.user.ip_address
    if ip_address not in object.hits.all() and object.is_published == True:
        object.hits.add(ip_address)
        Blog.objects.filter(slug=slug).update(num_hits=F('num_hits') + 1)
        COUNT_VIEWS += 1 
        if COUNT_VIEWS >= 1000:
            COUNT_VIEWS = 0
            user = Profile.objects.get(id = object.author.id)
            if SuperAccount.objects.filter(user=user).exists():  
                super_user = SuperAccount.objects.get(user=user)
                if super_user.super_account == "D":
                    user.amount += 200000
                    user.save()
                elif super_user.super_account == "S":
                    user.amount += 50000
                    user.save()
                else:
                    user.amount += 100000
                    user.save()
    context = {
        "object": object,
        "comments": item,
        "lencomments": len(BlogComment.objects.filter(blog=object)),
        "crn_user": profile,
        "author": author,
    }
    return render(request, "detail.html", context)


@login_required
@check_profile
def deletecomment(request, slug):
    comment = BlogComment.objects.get(id=slug)
    profile = Profile.objects.get(user=request.user)
    if comment.user == profile:
        comment.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return render(request, "404.html", status=404)


@login_required
@check_profile
def reply(request, id):
    if request.method == "POST":
        text = request.POST.get("text")
        if text.strip() == "":
            messages.error(request, "لطفا فضاهای خالی را از بین ببرید")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            comment = BlogComment.objects.get(id=id)
            profile = Profile.objects.get(user=request.user)
            object = BlogComment.objects.create(
                user=profile, blog=comment.blog, text=text, parent=comment
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
