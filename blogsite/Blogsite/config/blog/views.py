
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog , Category
# Create your views here.

def home(request):
    blog_list = Blog.objects.Published()
    pageinetoir = Paginator(blog_list,3)
    page_number = request.GET.get("page")
    blogs = pageinetoir.get_page(page_number)
    context = {
        'blogs':blogs,
    }
    return render(request,'index.html',context)


def detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request,'post.html',context)

def category(request,slug):
    category = Category.objects.get(slug = slug)
    blog_list = category.blogs.Published()
    pageinetoir = Paginator(blog_list,3)
    page_number = request.GET.get("page")
    blog = pageinetoir.get_page(page_number)
    context = {
             "category":category,
             "blogs":blog
    }     
    return render(request,'category.html',context)
