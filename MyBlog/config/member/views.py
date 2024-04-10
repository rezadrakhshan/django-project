from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import random
import string
from django.core.mail import send_mail
from .models import *
from blog.models import *
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from shop.models import Order

# Create your views here.


def check_profile(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            messages.error(request, "کاربر گرامی لطفا پروفایل خود را بسازید")
            return redirect("member:profile")
        return view_func(request, *args, **kwargs)

    return wrapper


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if (
            username.strip() == ""
            or email.strip() == ""
            or password.strip() == ""
            or password2.strip() == ""
        ):
            messages.error(request, "لطفا فضاهای خالی را از بین ببرید")
            return redirect("member:register")
        else:
            if password.strip() == password2.strip() and len(password.strip()) >= 4:
                if User.objects.filter(username=username.strip()).exists():
                    messages.error(request, "نام کاربری تکراری میباشد")
                    return redirect("member:register")
                elif User.objects.filter(email=email.strip()).exists():
                    messages.error(request, "ایمیل تکراری میباشد")
                    return redirect("member:register")

                else:
                    user_object = User.objects.create(
                        username=username.strip(),
                        email=email.strip(),
                        password=make_password(password.strip()),
                    )
                    user_object.save()
                    code = "".join(random.choices(string.digits, k=4))
                    object = Code.objects.create(code=code)
                    object.save()
                    html_content = render_to_string(
                        "email/confirm_code.html", {"code": code}
                    )
                    text_content = strip_tags(html_content)
                    msg = EmailMultiAlternatives(
                        "کد تایید ورود به کد بیان",
                        text_content,
                        "theweblogfromiran@gmail.com",
                        [user_object.email],
                    )
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    return redirect("member:check", username, email, object.id)
            else:
                messages.error(request, "لطفا پسورد را به درستی وارد کنید")
                return redirect("member:register")

    else:
        return render(request, "member/register.html")


def check(request, username, email, id):
    code = Code.objects.get(id=id)
    user = User.objects.get(username=username)
    context = {"user": user}
    if request.method == "POST":
        num = request.POST.get("num")
        print(code, num)
        if num == code.code:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return redirect("member:profile")
        else:
            messages.error(request, "لطفا کد را به درستی وارد کنید")
    return render(request, "member/check.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect("member:login")


@login_required
def profile(request):
    if request.user.is_staff or request.user.is_superuser:
        if Profile.objects.filter(user=request.user).exists():
            labels = ["منتشره شده", "منتشر نشده"]
            publish = Blog.objects.filter(is_published=True)
            draft = Blog.objects.filter(is_published=False)
            data = [len(publish), len(draft)]
            top_labels = []
            top_data = []
            blog = Blog.objects.filter(is_published=True).order_by("-num_hits")[:4]
            for i in blog:
                top_labels.append(i.title)
                top_data.append(i.num_hits)
            order_label = [
                "در حال بررسی",
                "در حال اماده سازی",
                "ارسال شده",
                "تحویل داده شده",
            ]
            order_data = [
                len(Order.objects.filter(status="P")),
                len(Order.objects.filter(status="PR")),
                len(Order.objects.filter(status="S")),
                len(Order.objects.filter(status="D")),
            ]

            context = {
                "product": len(Order.objects.all()),
                "blog": len(Blog.objects.all()),
                "comment": len(BlogComment.objects.all()),
                "user": len(Profile.objects.all()),
                "labels": labels,
                "data": data,
                "top_labels": top_labels,
                "top_data": top_data,
                "order_labels":order_label,
                "order_data":order_data,
            }
            return render(request, "registration/home.html", context)
        else:
            profile = Profile.objects.create(
                user=request.user,
                first_name=request.user.first_name,
                last_name=request.user.last_name,
                user_name=request.user.username,
                email=request.user.email,
                address=request.user.first_name,
            )
            return render(request, "registration/home.html")
    context = {}
    try:
        profile_obj = Profile.objects.get(user=request.user)
        context["user"] = profile_obj
    except:
        pass
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user_name = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        if (
            first_name.strip() == ""
            or last_name.strip() == ""
            or user_name.strip() == ""
            or email.strip() == ""
            or address.strip() == ""
        ):
            messages.error(request, "لطفا فضا های خالی را از بین ببرید")
            return redirect("member:profile")
        try:
            user = Profile.objects.get(user=request.user)
            user.first_name = first_name
            user.last_name = last_name
            user.user_name = user_name
            user.email = email
            user.address = address
            request.user.email = email
            request.user.save()
            user.save()
            messages.info(request, "تغییرات با موفقیت اعمال گردید")
            return redirect("member:profile")
        except:
            if Profile.objects.filter(user_name=user_name).exists():
                messages.error(request, "نام کاربری توسط فردی دیگر استفاده شده است")
                return redirect("member:profile")
            object = Profile.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                email=email,
                address=address,
            )
            request.user.email = email
            request.user.save()
            messages.info(request, "پروفایل با موفقیت ساخته شد")
            return redirect("member:profile")

    return render(request, "member/profile.html", context)


@login_required
@check_profile
def change(request):
    if request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1.strip() == password2.strip() and len(password1.strip()) > 4:
            user = User.objects.get(username=request.user.username)
            user.password == make_password(password1.strip())
            user.save()
            messages.success(request, "گذرواژه با موفقیت تغییر کرد")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "مقادیر وارد شده صحیح نمی باشند")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    return render(request, "member/change_password.html")


@login_required
@check_profile
def myblog(request):
    user = Profile.objects.get(user=request.user)
    blog = Blog.objects.filter(author=user)
    context = {"blogs": blog}
    return render(request, "member/myblog.html", context)


@login_required
@check_profile
def user_profile(request, id):
    user = Profile.objects.get(user=request.user)
    following = Profile.objects.get(id=id)
    user_follower = FollowersCount.objects.filter(user=following)
    user_following = FollowersCount.objects.filter(follower=following)
    text = "دنبال کردن"
    if FollowersCount.objects.filter(follower=user, user=following).exists():
        text = "دنبال میشود"
    if int(id) == int(user.id):
        return redirect("member:profile")
    else:
        user = Profile.objects.get(id=id)
        blog = Blog.objects.filter(author=user, is_published=True)
        context = {
            "user": user,
            "blogs": blog,
            "text": text,
            "user_follower": user_follower,
            "user_following": user_following,
        }

    return render(request, "user_profile.html", context)


def follow(request, id):
    following = Profile.objects.get(id=id)
    follower = Profile.objects.get(user=request.user)
    if int(follower.id) == int(id):
        return render(request, "404.html", status=404)
    try:
        delete_follower = FollowersCount.objects.get(follower=follower, user=following)
        delete_follower.delete()
    except:
        new_follower = FollowersCount.objects.create(follower=follower, user=following)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def top_user(request):
    top_authors = (
        Blog.objects.values("author")
        .annotate(total_hits=Count("hits"))
        .order_by("-total_hits")
    )[:50]
    users = []
    for author in top_authors:
        author_profile = Profile.objects.get(id=author["author"])
        users.append(
            {
                "profile": author_profile,
                "email": author_profile.email,
                "hits": author["total_hits"],
            }
        )

    context = {"users": users}
    return render(request, "member/top_user.html", context)
