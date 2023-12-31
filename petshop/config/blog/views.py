from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def blogs(request):
    category = Category.objects.all()
    blog_list = Blog.objects.filter(publish=True)
    paginator = Paginator(blog_list, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)

    context = {"blogs": blog, "categories": category, "recents": Blog.objects.all()[:4]}
    return render(request, "blog.html", context)


@login_required(login_url="login")
def detail(request, id):
    blogdetail = Blog.objects.get(id=id)
    category = Category.objects.all()
    b_comment = Comment.objects.filter(blog=blogdetail)
    ip_address = request.user.ip_address
    if ip_address not in blogdetail.hits.all():
        blogdetail.hits.add(ip_address)
    context = {
        "blogdetail": blogdetail,
        "categories": category,
        "recents": Blog.objects.all()[:4],
        "comments": b_comment,
        "lencomment": len(b_comment),
    }
    return render(request, "detail.html", context)


@login_required(login_url="login")
def category(request, title):
    filtercategory = Category.objects.get(title=title)
    blog_list = Blog.objects.filter(category=filtercategory)
    paginator = Paginator(blog_list, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)
    category = Category.objects.all()
    context = {
        "blogs": blog,
        "categories": category,
        "recents": Blog.objects.filter(category=filtercategory)[:4],
    }
    return render(request, "blog.html", context)


@login_required(login_url="login")
def comment(request, id):
    post = Blog.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        text = request.POST["text"]
        Comment.objects.create(name=name, body=text, blog=post)
        return redirect("blog:blogdetail", id)
