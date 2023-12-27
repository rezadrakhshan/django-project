from django.urls import path,include
from . import views


app_name = "movie"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("like-post/<movie_id>", views.like, name="like"),
    path("Wish/<movie_id>", views.wish, name="wish"),
    path("WishList/", views.wishlist, name="wishlist"),
    path("Share/email/<pk>", views.share_email, name="email"),
    path("Share/telegram/<pk>", views.share_telegram, name="telegram"),
    path("movie/all/popular", views.allmovie, name="popular"),
    path("movie/all/anime", views.allmovie, name="anime"),
    path("movie/all/sport", views.allmovie, name="sport"),
    path("movie/all/action", views.allmovie, name="action"),
    path("movie/search/", views.search, name="search"),
    path("movie/contact/", views.contact, name="contact"),
]
