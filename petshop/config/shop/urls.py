from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("team/", views.team, name="team"),
    path("price/", views.price, name="price"),
    path("contact/",views.contact,name="contact")
]
