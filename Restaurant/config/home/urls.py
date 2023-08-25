from django.urls import path
from . import views
app_name = "home"



urlpatterns = [
    path("",views.home,name="home"),
    path("aboutus/",views.about,name="about"),
    path("service/",views.service,name="service"),
    path("chefs/",views.chefs,name="chefs")
]
