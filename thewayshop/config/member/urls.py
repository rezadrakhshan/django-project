from django.urls import path
from .views import *

app_name = "member"

urlpatterns = [
    path("login/",user_login,name="login"),
    path("register/",register,name="register"),
    path("logout/",user_logout,name="logout"),
]
