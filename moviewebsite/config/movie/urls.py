from django.urls import path
from . import views

app_name = "movie"
urlpatterns = [
    path('', views.movie,name="home"),
    path('listmovie/', views.listmovie,name="listmovie"),
    path('<slug>/', views.moviedetail,name="moviedetail"),
    path('video/<slug>/', views.movie_file,name="moviefile"),
    path('category', views.category,name="category"),
    path('category/<title>',views.ctcategory,name="ctdetail"),
    path('company',views.company,name="company"),
    path('company/<name>',views.cmlist,name="cmlist"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('about',views.about,name="about"),
    path('search',views.search,name="search"), 

]