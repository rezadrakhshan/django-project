from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("add-blog/", views.addblog, name="addblog"),
    path("remove-blog-<slug>/", views.removeblog, name="removeblog"),
    path("edit-blog-<slug>/", views.editblog, name="editblog"),
    path("blog-detail-<slug>/", views.detail, name="detail"),
    path("comment-remove-<slug>/", views.deletecomment, name="deletecomment"),
    path("reply-to-<id>", views.reply, name="reply"),
]
