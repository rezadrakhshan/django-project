from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("blogs/",views.blogs,name="blogs"),
    path("detail/<id>/",views.detail,name="blogdetail"),
    path("category/<title>",views.category,name="category"),
    path("comment/<id>",views.comment,name="comment")
]
