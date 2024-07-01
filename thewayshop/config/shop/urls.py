from django.urls import path
from .views import *

app_name = "shop"
urlpatterns = [
    path("detail-<id>/", detail, name="detail"),
    path("add-wish-item-<product>",wishitem,name="wish"),
    path("remove-whish-item-<pk>",removewish,name="removewish"),
    path("wish-list",wishlist,name="wishlist"),
    path("category-<slug>",category,name="category"),
    path("filter-price",filter_price,name="filter_price"),
    path("search-products",search,name="search"),
    path("add-cart",add_cart,name="add_cart"),
    path("cart",cart,name="cart"),
    path("remove-cart-<slug>",remove_cart,name="remove_cart"),
    path("add-coupon",use_token,name="add_coupon")
]
