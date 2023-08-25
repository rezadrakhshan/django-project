from django.urls import path
from . import views

app_name = "reserve"
urlpatterns = [
    path("addreserve/",views.add,name="add")
]
