from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('',home,name="home"),
    path('contact-us/',contact_us,name="contact"),
]
