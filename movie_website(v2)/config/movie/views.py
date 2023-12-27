from django.shortcuts import render, redirect
from .models import *
from member.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.


@login_required(login_url="account_signup")
def home(request):
    slider = Movie.objects.all()[:4]
    popular = Movie.objects.order_by("-no_likes")
    context = {
        "slider": slider,
        "popular": popular,
    }
    try:
        cat = Category.objects.get(title="anime")
        if cat:
            anime = Movie.objects.filter(Genres=cat).order_by("-imdb")
            context["anime"] = anime
        cat_sport = Category.objects.get(title="sport")
        if cat_sport:
            sport = Movie.objects.filter(Genres=cat_sport).order_by("-imdb")
            context["sport"] = sport
        best = Movie.objects.all().order_by("-imdb")[:1]
        context["best"] =  best
        cat_action = Category.objects.get(title="action")
        if cat_action:
            action = Movie.objects.filter(Genres=cat_action).order_by("-imdb")
            context["action"] = action
    except:
        print("")
    return render(request, "index.html", context)


@login_required
def like(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    is_liked = Like.objects.filter(movie_id=movie.id, user=request.user.username)
    if is_liked.exists():
        is_liked.delete()
        movie.no_likes -= 1
        movie.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    elif not is_liked.exists():
        new_like = Like.objects.create(movie_id=movie.id, user=request.user.username)
        new_like.save()
        movie.no_likes += 1
        movie.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="account_signup")
def wish(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    is_wish = Wish.objects.filter(movie=movie, user=request.user.id)
    if is_wish.exists():
        is_wish.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    elif not is_wish.exists():
        new_wish = Wish.objects.create(movie=movie, user=request.user.id)
        new_wish.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def wishlist(request):
    wish = Wish.objects.filter(user=request.user.id)
    context = {"movie": wish}
    return render(request, "wish.html", context)


def share_email(request, pk):
    movie = Movie.objects.get(id=pk)
    text_mail = f"Hello, sir!!\n\n\nYour friend {request.user.username} wants to invite you to watch the {movie.title}\nAccept your friend invitation and come to Netflix to watch this movie in the best quality\n\n\nTo access these movies and more information, you can visit our website or send us your email so that we can send you the download link of the new movies.\n\n\n\n Thanks for Support Us\nNetflix Team"
    context = {"movie": movie, "text": text_mail, "img": movie.poster}
    return render(request, "share.html", context)


def share_telegram(request, pk):
    movie = Movie.objects.get(id=pk)
    text = f"Try {movie.title} in Netflix now"
    context = {"movie": movie, "text": text}
    return render(request, "share.html", context)


def allmovie(request):
    url_name = resolve(request.path).url_name
    context = {}
    if url_name == "popular":
        popular = Movie.objects.order_by("-no_likes")
        context["popular"] = popular
    if url_name == "anime":
        cat = Category.objects.get(title="anime")
        anime = Movie.objects.filter(Genres=cat).order_by("-imdb")
        context["anime"] = anime
    if url_name == "sport":
        cat_sport = Category.objects.get(title="sport")
        sport = Movie.objects.filter(Genres=cat_sport).order_by("-imdb")
        context["sport"] = sport
    if url_name == "action":
        cat_action = Category.objects.get(title="action")
        action = Movie.objects.filter(Genres=cat_action).order_by("-imdb")
        context["action"] = action
    return render(request, "movielist.html", context)


def search(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        item = Movie.objects.filter(title__icontains=name)
        context["item"] = item
    return render(request, "movielist.html", context)


def contact(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        message = request.POST["message"]
        send_to = "videostream476@gmail.com"
        s = "videostream476@gmail.com"
        from_email = request.POST["send_to"]
        msg = f"this email is from {from_email}\n{message}"
        if subject and message and send_to:
            try:
                send_mail(subject, msg, s, [send_to])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
            messages.info(request,"Email sent")
            return redirect("movie:contact")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")
    return render(request, "contact.html")
