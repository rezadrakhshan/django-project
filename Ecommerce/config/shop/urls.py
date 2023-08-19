from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path('',views.home,name="home"),
    path('mycart/unpaid/',views.cart,name="cart"),
    path('mycart/paid/',views.Paid,name="paid"),
    path('checkout/<slug>/',views.checkout,name="checkout"),
    path('order/remove/<slug>/',views.remove,name="remove"),
    path('contact-us/',views.contact_us,name="contact_us"),
    path('item/search/',views.search,name="search"),
    path('female/',views.female,name="female"),
    path('female/search/',views.sfemale,name="femalesearch"),
    path('man/search/',views.sman,name="mansearch"),
    path('man/',views.man,name="man"),
    path('<slug>/',views.category,name="category"),
    path('item/<slug>/',views.detail,name="detail"),
    path('acount/register/',views.register,name="register"),
    path('acount/login/',views.login,name="login"),
    path('female/<slug>/',views.cfemale,name="categoryfemale"),
    path('man/<slug>/',views.cman,name="categoryman"),
]
