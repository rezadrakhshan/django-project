from django.urls import path
from . import views
from .views import BestArticlesView
app_name = "main"

urlpatterns = [
    path("", views.welcome_page, name="welcome_page"),
    path("home", BestArticlesView.as_view(), name="home"),
    path("contact-us", views.contact_us, name="contact"),
    path("category/<slug>/", views.category, name="category"),
    path("search/", views.search, name="search"),
    path("super-account-<id>/", views.super_account_user, name="super_account"),
]
