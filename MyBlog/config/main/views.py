from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Message
import json
from blog.models import Blog, Category
from django.core.paginator import Paginator
from member.models import Profile, FollowersCount, SuperAccount
from shop.models import Products
from django.views.generic import ListView
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from member.views import check_profile
from django.utils.decorators import method_decorator


def welcome_page(request):
    product = len(Products.objects.all())
    user = len(Profile.objects.all())
    blog = len(Blog.objects.filter(is_published=True))
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        s = "theweblogfromiran@gmail.com"
        if name.strip() == "" or message.strip() == "" or email.strip() == "":
            messages.error(request, "لطفا تمام مقادیر را وارد کنید")
            return redirect("main:welcome_page")
        else:
            object = Message.objects.create(name=name, email=email, text=message)
            l = Message.objects.all()
            if len(l) == 10:
                msg = []
                for i in l:
                    msg.append(f"{i.name}|{i.email}|{i.text}")
                formatted_msg = json.dumps(msg, indent=2)
                send_mail(
                    "نظرات کاربران",
                    str(formatted_msg),
                    "theweblogfromiran@gmail.com",
                    ["theweblogfromiran@gmail.com"],
                    fail_silently=False,
                )
                l.delete()
            html_content = render_to_string("email/email.html")
            txt_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(
                "با تشکر از نظرات شما", txt_content, s, [email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.info(request, "پیام شما با موفقیت ارسال شد")
            return redirect("main:welcome_page")
    context = {
        "product":product,
        "user":user,
        "blog":blog
    }
    return render(request,"welcome_page.html",context)

@method_decorator(login_required, name="dispatch")
@method_decorator(check_profile, name="dispatch")
class BestArticlesView(ListView):
    model = Blog
    template_name = "index.html"
    context_object_name = "object"

    def get_queryset(self):
        now = timezone.now()
        week_start = now - timedelta(days=now.weekday())
        week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        year_start = now.replace(
            month=1, day=1, hour=0, minute=0, second=0, microsecond=0
        )

        best_in_week = Blog.objects.filter(
            created_at__gte=week_start, created_at__lt=now, is_published=True
        ).order_by("-num_hits")

        best_in_month = Blog.objects.filter(
            created_at__gte=month_start, is_published=True
        ).order_by("-num_hits")

        best_in_year = Blog.objects.filter(
            created_at__gte=year_start, is_published=True
        ).order_by("-num_hits")

        user = Profile.objects.get(user=self.request.user)
        myblog = Blog.objects.filter(author=user)

        user_profile = Profile.objects.get(user=self.request.user)
        following_profiles = FollowersCount.objects.filter(
            follower=user_profile
        ).values_list("user", flat=True)
        articles = Blog.objects.filter(author__in=following_profiles, is_published=True)

        return {
            "best_in_week": best_in_week,
            "best_in_month": best_in_month,
            "best_in_year": best_in_year,
            "blogs": myblog,
            "follower_blog": articles,
        }


@login_required
@check_profile
def contact_us(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        name = request.POST["name"]
        message = request.POST["message"]
        s = "theweblogfromiran@gmail.com"
        from_email = request.POST["email"]
        if name.strip() == "" or message.strip() == "" or from_email.strip() == "":
            messages.error(request, "لطفا تمام مقادیر را وارد کنید")
            return redirect("main:contact")
        else:
            object = Message.objects.create(name=name, email=from_email, text=message)
            l = Message.objects.all()
            if len(l) == 10:
                msg = []
                for i in l:
                    msg.append(f"{i.name}|{i.email}|{i.text}")
                formatted_msg = json.dumps(msg, indent=2)
                send_mail(
                    "نظرات کاربران",
                    str(formatted_msg),
                    "theweblogfromiran@gmail.com",
                    ["theweblogfromiran@gmail.com"],
                    fail_silently=False,
                )
                l.delete()
            html_content = render_to_string("email/email.html")
            txt_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(
                "با تشکر از نظرات شما", txt_content, s, [profile.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.info(request, "پیام شما با موفقیت ارسال شد")
            return redirect("main:contact")
    return render(request, "contact_us.html")


def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)


@login_required
@check_profile
def category(request, slug):
    object = Category.objects.get(id=slug)
    context = {"category": object}
    blog_list = Blog.objects.filter(category=object, is_published=True)
    paginator = Paginator(blog_list, 8)
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)
    context["blogs"] = blog
    if request.method == "POST":
        word = request.POST.get("word")
        blog_list = Blog.objects.filter(
            title__icontains=word, is_published=True, category=object
        )
        paginator = Paginator(blog_list, 8)
        page_number = request.GET.get("page")
        search = paginator.get_page(page_number)
        context["blogs"] = search

    return render(request, "index.html", context)


@login_required
@check_profile
def search(request):
    if request.method == "POST":
        word = request.POST.get("word")
        profile = Profile.objects.filter(user_name__icontains=word)
        users = []
        for i in profile:
            follower = FollowersCount.objects.filter(follower=i).count()
            following = FollowersCount.objects.filter(user=i).count()
            users.append({"profile": i, "follower": follower, "following": following})
        blog_list = Blog.objects.filter(title__icontains=word, is_published=True)
        context = {
            "blogs": blog_list,
            "word": word,
            "profiles": users,
        }
    return render(request, "search.html", context)


@login_required
@check_profile
def super_account_user(request, id):
    profile = Profile.objects.get(user=request.user)
    if profile.amount >= 100000 and id == "G":
        if SuperAccount.objects.filter(user=profile).exists():
            messages.error(request, "کاربر گرامی شما در حال حاضر بسته ای دارید")
            return redirect("main:home")
        else:
            super = SuperAccount.objects.create(user=profile, super_account=str(id))
            messages.success(request,"کاربر گرامی بسته شما با موفقیت خریداری شد")
            return redirect("main:home")
    elif profile.amount >= 200000 and id == "D":
        if SuperAccount.objects.filter(user=profile).exists():
            messages.error(request, "کاربر گرامی شما در حال حاضر بسته ای دارید")
            return redirect("main:home")
        else:
            super = SuperAccount.objects.create(user=profile, super_account=str(id))
            messages.success(request,"کاربر گرامی بسته شما با موفقیت خریداری شد")
            return redirect("main:home")
    elif profile.amount >= 50000 and id == "S":
        if SuperAccount.objects.filter(user=profile).exists():
            messages.error(request, "کاربر گرامی شما در حال حاضر بسته ای دارید")
            return redirect("main:home")
        else:
            super = SuperAccount.objects.create(user=profile, super_account=str(id))
            messages.success(request,"کاربر گرامی بسته شما با موفقیت خریداری شد")
            return redirect("main:home")    
    else:    
        messages.error(request,"اعتبار شما کافی نیست لطفا حساب خود را شارژ کنید")
        return redirect("main:home")
