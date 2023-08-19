from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Create your views here.


def home(request):
    category = Category.objects.all()
    item = Item.objects.filter(available=True)

    context = {
        "category":category,
        "item":item,

    }
    return render(request,"index.html",context)

def female(request):
    category = Category.objects.all()
    product_item = Item.objects.filter(gender="F")

    context = {
        "product_item":product_item,
        "category":category,

    }
    return render(request,"female.html",context)

def cfemale(request,slug):
    categorys = Category.objects.all()
    cat = Category.objects.get(slug=slug)
    product = Item.objects.filter(category=cat,gender="F")

    context = {
        "categorys":categorys,
        "product":product,

    }
    return render(request,"category/female.html",context)
    


def man(request):
    category = Category.objects.all()
    product_item = Item.objects.filter(gender="M")

    context = {
        "product_item":product_item,
        "category":category,

    }
    return render(request,"man.html",context)

def cman(request,slug):
    categorys = Category.objects.all()
    cat = Category.objects.get(slug=slug)
    product = Item.objects.filter(category=cat,gender="M")

    context = {
        "categorys":categorys,
        "product":product,

    }
    return render(request,"category/man.html",context)

def category(request,slug):
    categorys = Category.objects.all()
    cat = Category.objects.get(slug=slug)
    product = Item.objects.filter(category=cat)

    context = {
        "cat":cat,
        "product":product,
        "categorys":categorys,

    }
    return render(request,"category.html",context)
@login_required(login_url="shop:register")
def detail(request,slug):
    detail = Item.objects.get(slug=slug)
    if request.method =="POST":
        number = request.POST['number']
        mylist = []
        for i in range(int(number)):
            order = Order.objects.create(user=request.user,item=detail,status="Unpaid",name=detail.name,image=detail.image,category=detail.category,price=detail.price)
            mylist.append(order)
        return redirect("shop:cart")
    context = {
        "detail":detail,
    }
    return render(request,"detail.html",context)
def register(request):
    if request.method=="POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password==password2 and len(password) > 4:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Taken")
                return redirect("shop:register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("shop:register")
            else:
                user = User.objects.create(username=username,email=email,password=make_password(password))
                user.save()
                auth.login(request,user)
                return redirect("shop:home")
        else:
            messages.info(request,"passwords are not the same(len password > 4)")
            return redirect("shop:register")
    else:
        return render(request,"register.html")
    
def login(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"credentials are invalid")
            return redirect("shop:login")
    else:
        return render(request,"login.html")

def search(request):
    order = Order.objects.filter(user=request.user)
    if request.method == "POST":
        title = request.POST['title']
        object = Item.objects.filter(name__icontains = title,available=True)
        context = {
            "object":object,

        }
    return render(request,"search/search.html",context)
def sfemale(request):
    order = Order.objects.filter(user=request.user)
    if request.method == "POST":
        title = request.POST['title']
        female = Item.objects.filter(name__icontains = title,available=True,gender="F")
        context = {
            "female":female,

        }
    return render(request,"search/search.html",context)
def sman(request):

    if request.method == "POST":
        title = request.POST['title']
        man = Item.objects.filter(name__icontains = title,available=True,gender="M")
        context = {
            "man":man,
        }
    return render(request,"search/search.html",context)

def contact_us(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        msg = request.POST['message']
        password = "viqkzykvtomxbxpb"
        me = "ecommerceforreza@gmail.com"
        you ="ecommerceforreza@gmail.com"
        email_body = "name:{0}\nemail:{1}\nphone:{2}\nsubject:{3}\nmessage:{4}".format(name, email, phone, subject, msg)
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
            print(f"email sent: {email_body}")
        except Exception as e:
            print(f'error in sending email: {e}')

        


    return render(request,"contact-us.html")
@login_required(login_url="shop:register")
def cart(request):
    order = Order.objects.filter(user=request.user,status="Unpaid")
    context = {
        "order":order,
    }
    return render(request,"mycart.html",context)
@login_required(login_url="shop:register")
def Paid(request):
    order = Order.objects.filter(user=request.user, status="Paid")
    context = {
        "order":order
    }
    return render(request,"paid.html",context)


def remove(request,slug):
    item = Order.objects.filter(slug=slug)
    item.delete()
    return redirect("shop:cart")

def checkout(request,slug):
    order = Order.objects.get(slug=slug)
    if request.method=="POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        adress = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        zipcode = request.POST['zip']
        name_on_card = request.POST['name_on_card']
        credit_card_number = request.POST['credit_card_number']
        Expiration = request.POST['Expiration']
        cvv = request.POST['CVV']
        new_order = Order.objects.create(user=request.user,item=order.item,status="Paid",name=order.name,image=order.image,category=order.category,price=order.price)
        checked = CheckoutOrder.objects.create(user=request.user, order=new_order, first_name=first_name, last_name=last_name, username=username, email=email, adress=adress, country=country, state=state, zipcode=zipcode, name_on_card=name_on_card, credit_card_number=int(credit_card_number), Expiration=Expiration, CVV=cvv)
        order.delete()
        return redirect("shop:paid")
    return render(request,"checkout-page.html")