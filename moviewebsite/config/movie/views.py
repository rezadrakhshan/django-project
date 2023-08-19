from django.shortcuts import render,redirect
from movie.models import Movie,Message,Category,Company
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="movie:register")
def movie(request):
    list_movie = Movie.objects.filter(status="published")
    paginator = Paginator(list_movie,6)
    page_number = request.GET.get("page")
    movie = paginator.get_page(page_number)
    list_cm = Movie.objects.filter(status="coming soon")
    special_offers = Movie.objects.filter(special_offers=True,status = "published")
    context = {
        "movies":movie,
        "list_cm":list_cm,
        "special_offers":special_offers,
        "l_movies":len(movie),
        "l_listcm":len(list_cm),
        "l_special_offers":len(special_offers)
    }
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        message_text = request.POST["message"]
        message_user = Message.objects.create(name=name,phone=phone,email=email,message=message_text)
        message_user.save()
    return render(request,"index.html",context)
    
@login_required(login_url="movie:register")
def listmovie(request):
    listmovie = Movie.objects.filter(status="published")
    context = {
        'listmovies':listmovie
    }
    return render(request,"movie.html",context)


    


@login_required(login_url="movie:register")
def moviedetail(request, slug):
    detail = Movie.objects.get(slug=slug)
    context = {
        "detail":detail
    }
    return render(request,"moviedetail.html",context)
@login_required(login_url="movie:register")
def movie_file(request, slug):
    detail = Movie.objects.get(slug=slug)
    context = {
        "detail":detail
    }
    return render(request,"video/moviefile.html",context)
@login_required(login_url="movie:register")
def category(request):
    category = Category.objects.all()
    context = {
        "categories":category
    }
    return render(request,"category.html",context)
@login_required(login_url="movie:register")
def ctcategory(request,title):
    category_list = Movie.objects.filter(Category=title)

    context = {
        'category_lists':category_list
    }
    return render(request,"ctdetail.html",context)
@login_required(login_url="movie:register")
def company(request):
    company = Company.objects.all()
    context = {
        "company":company
    }
    return render(request,"company.html",context)
@login_required(login_url="movie:register")
def cmlist(request,name):
    company_list = Movie.objects.filter(company=name)
    context = {
        "company_list":company_list
    }
    return render(request,"cmdetail.html",context)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]

        if password==password2 and len(password) >= 4:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken")
                return redirect("movie:register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("movie:register")
            else:
                user = User.objects.create(username=username,email=email,password=make_password(password))
                user.save()
                auth.login(request,user)
                return redirect("movie:home")
        else:
            messages.info(request,"passwords are not the same")
            return redirect("movie:register")
    else:
        return render(request,"register.html")
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"credentials are invalid")
            return redirect("movie:login")
    else:
        return render(request,"login.html")
    
@login_required(login_url="movie:register")
def logout(request):
    auth.logout(request)
    return redirect("movie:login")
@login_required(login_url="movie:register")
def about(request):
    return render(request,"about.html")
@login_required(login_url="movie:register")
def search(request):
    if request.method == "POST":
        title = request.POST['title']
        title_objects = Movie.objects.filter(movie_name__icontains = title,status = "published")
        context = {
            'title_objects':title_objects
        }
    return render(request,"search.html",context)