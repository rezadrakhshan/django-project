from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
    path("",views.home,name="home"),
    path("aboutus/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("<slug>/",views.detail,name="detail"),
    path("author/<name>",views.author,name="author"),
    path("category/<name>",views.category,name="category"),
]
