from django.shortcuts import render
from .models import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

    
def home(request):
    category = Category.objects.all()
    blog_list = Blog.objects.filter(status="p")
    paginator = Paginator(blog_list, 3 )  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)
    return render(request, "index.html", {"blog": blog,"category":category})


def detail(request,slug):
    category = Category.objects.all()
    blog = Blog.objects.get(slug=slug)
    context = {
        "blog":blog,
        "category":category
    }
    return render(request,"post.html",context)

def author(request,name):
    category = Category.objects.all()
    user = User.objects.get(username=name)
    author_list = Blog.objects.filter(author=user)
    paginator = Paginator(author_list, 3 )  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    author = paginator.get_page(page_number)
    context = {
        "author":author,
        "user":user,
        "category":category
    }
    return render(request,"author.html",context)

def about(request):
    category = Category.objects.all()
    context = {
        "category":category
    }
    return render(request,"about.html",context)

def contact(request):
    category = Category.objects.all()
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        msg = request.POST['message']
        password = "fhxumnbwwqdthjyl"
        me = "myblogsite4all@gmail.com"
        you ="myblogsite4all@gmail.com"
        email_body = "name:{0}\nemail:{1}\nphone:{2}\nmessage:{3}\nsubject{4}".format(name, email, phone, msg, subject)
        message = MIMEMultipart('alternative' , None,
        [MIMEText(email_body, "html")])
        message['subject'] = subject
        message['From'] = email
        message["To"] = you
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(me, password)
            server.sendmail(email, you, message.as_string())
            server.quit()
            messages.info(request,"Email sent")
        except Exception as e:
            messages.info(request,"The email was not sent. pleas try again later")
    context = {
        "category":category
    }
    return render(request,"contact.html",context)

def category(request,name):
    category = Category.objects.all()
    item = Category.objects.get(name=name)
    blog_list = Blog.objects.filter(category=item)
    paginator = Paginator(blog_list, 3 )  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)
    context = {
        "item":item,
        "blog":blog,
        "category":category
    }
    return render(request,"category.html",context)