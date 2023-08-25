from django.urls import path
from . import views

app_name = "comment"

urlpatterns = [
    path("addcomment/",views.comment,name="comment"),
    path("allcomment/",views.allcomment,name="allcomment"),
]
