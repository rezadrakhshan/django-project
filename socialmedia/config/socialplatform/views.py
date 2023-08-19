from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile,Post,Like,Comment,FollowersCount
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from itertools import chain
import random


@login_required(login_url="socialplatform:login")
def home(request):
    user_profile = Profile.objects.get(username = request.user)
    post = Post.objects.all()
    userfollowing = FollowersCount.objects.filter(follower=request.user.username)
    all_users = User.objects.all()
    user_following_all = []
    for user in userfollowing:
        user_list  = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in (list(new_suggestions_list)) if (x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)
    for ids in username_profile:
        profile_lists = Profile.objects.filter(user_id=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))
    context = {
        'userprofile':user_profile,
        'posts':post,
        'crn_user':request.user.username,
        'suggestions_username_profile_list':suggestions_username_profile_list
    }
    return render(request,"index.html",context)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 and len(password) >= 4:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username has been taken")
                return redirect("socialplatform:signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email has been taken")
                return redirect("socialplatform:signup")

            else:
                user_object = User.objects.create(username=username,email=email,password=make_password(password))
                user_object.save()
                user = User.objects.get(username=username)
                user_profile = Profile.objects.create(username=user)
                user_profile.save()
                auth.login(request,user)
                return redirect("socialplatform:setting")
        else:
            messages.info(request,"password error")
            return redirect("socialplatform:signup")

    else:
        return render(request,"signup.html")
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("socialplatform:home")
        else:
            messages.info(request,"invalid credentials")
            return redirect("socialplatform:login")
    return render(request,"signin.html")

@login_required(login_url="socialplatform:login")
def logout(request):
    auth.logout(request)
    return render(request,"signin.html")

@login_required(login_url="socialplatform:login")
def setting(request):
    user_profile = Profile.objects.get(username = request.user)
    if request.method == "POST":
        if request.FILES.get("image") == None:
            user_profile.address = request.POST["location"]
            user_profile.bio = request.POST["bio"]
            user_profile.name = request.POST["name"]
            user_profile.save()
        elif request.FILES.get("image") != None:
            user_profile.image = request.FILES.get("image")
            user_profile.address = request.POST["location"]
            user_profile.bio = request.POST["bio"]
            user_profile.name = request.POST["name"]
            user_profile.save()
        
    return render(request,"setting.html",context={"profile":user_profile})

@login_required(login_url="socialplatform:login")
def profile(request, username):
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(username=user_object)
    user_posts = Post.objects.filter(username=user_profile.username.username)
    context = {
        "user_object":user_object,
        "user_profile":user_profile,
        "user_posts":user_posts,
        "posts":len(user_posts)
    }
    return render(request,"profile.html",context)


def upload(request):
    if request.method == 'POST':
        user = request.user.username
        caption = request.POST["caption"]
        image = request.FILES.get('image')
        new_post = Post.objects.create(username=user,caption=caption,image=image)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

def like(request, post_id):
    post = Post.objects.get(id=post_id)
    is_liked = Like.objects.filter(post_id=post.id,user=request.user.username)
    if is_liked.exists():
        is_liked.delete()
        post.no_likes -= 1
        post.save()
        return redirect('/')
    elif not is_liked.exists():
        new_like = Like.objects.create(post_id=post.id,user=request.user.username)
        new_like.save()
        post.no_likes += 1
        post.save()
        return redirect('/')
    
def comment(request):
    if request.method == "POST":
        comment = request.POST["comment"]
        post = request.POST["postid"]
        author  = request.user.username
        user = request.POST['postuser']
    
        post_id = Post.objects.get(id = post)
        new_comment = Comment.objects.create(comment=comment,author=author,user=user,post=post_id)
        new_comment.save()
        return redirect('/')
        
    
    else:
        return redirect('/')
    
def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

def dlcomment(request,comment_slug):
    comment = Comment.objects.get(slug=comment_slug)
    comment.delete()
    return redirect('/')

def follow(request):
    if request.method == "POST":
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower,user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower,user=user)
            new_follower.save()
            return redirect('/profile/'+user)

    else:
        return redirect("/")

def search(request):
    if request.method == "POST":
        name = request.POST["username"]
        user = Profile.objects.filter(name__icontains=name)
        context = {
            "user":user,
        }

    return render(request,"search.html",context)