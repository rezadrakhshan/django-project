from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Team, Service
from shop.models import Product
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.conf import settings
import time



# home page function
@login_required
def home(request):
    product = Product.objects.filter(avaible=True).order_by("-price")[:8]
    context = {
        "products":product,
    }
    return render(request, "index.html",context)


# about us page function
@login_required
def about(request):
    member = Team.objects.all()
    service = Service.objects.all()[:3]
    context = {
        "members": member,
        "services": service,
    }
    return render(request, "about.html", context)


@login_required
def service(request):
    member = Team.objects.all()
    service = Service.objects.all()
    context = {"members": member, "services": service}
    return render(request, "service.html", context)


#TODO: this code have a bug 
@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        html_content = render_to_string(
            "email/email.html", {"email": email, "message": message, "name": name}
        )
        txt_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            subject,
            txt_content,
            "theweblogfromiran@gmail.com",
            ["theweblogfromiran@gmail.com"],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        html_content2 = render_to_string("email/user_email.html")
        email = EmailMessage(subject, html_content2, "theweblogfromiran@gmail.com", [email])
        email.content_subtype = "html"
        email_sent = email.send()
        if email_sent:
            print("User email sent successfully.")
        else:
            print("Failed to send user email.")
        return redirect("main:contact")
    return render(request, "contact-us.html")
