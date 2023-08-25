from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("menu/",views.menu,name="menu"),
    path("lunch/",views.lunch,name="lunch"),
    path("dinner/",views.dinner,name="dinner"),
]
