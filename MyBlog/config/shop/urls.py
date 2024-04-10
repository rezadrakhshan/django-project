from django.urls import path
from . import views


app_name = "shop"

urlpatterns = [
    path("products/",views.products,name="products"),
    path("add-procurement-<id>/",views.add_procurement,name="add_procurement"),
    path("cart/",views.cart,name="cart"),
]
