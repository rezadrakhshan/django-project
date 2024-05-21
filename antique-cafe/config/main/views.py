from django.shortcuts import render, redirect
from menu.models import Coffee
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    coffee = Coffee.objects.filter(is_avaible=True)
    mylist = []
    j = 0
    is_right = 0
    for i in coffee:
        j += 1
        if j % 2 == 0:
            is_right = 1
            mylist.append(
                {
                    "name": i.name,
                    "small_price": i.small_price,
                    "medium_price": i.medium_price,
                    "large_price": i.large_price,
                    "image": i.image.url,
                    "is_right": is_right,
                }
            )
        else:
            is_right = 0
            mylist.append(
                {
                    "name": i.name,
                    "small_price": i.small_price,
                    "medium_price": i.medium_price,
                    "large_price": i.large_price,
                    "image": i.image.url,
                    "is_right": is_right,
                }
            )

    context = {"coffee": mylist}
    return render(request, "index.html", context)


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        html_content = render_to_string(
            "email.html", {"email": email, "message": message}
        )
        txt_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            "User Message",
            txt_content,
            "theweblogfromiran@gmail.com",
            ["theweblogfromiran@gmail.com"],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect("/")
