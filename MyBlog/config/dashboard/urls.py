from django.urls import path
from .views import *
app_name = "dashboard"
 
urlpatterns = [
    path("blog-list/",blog_list,name="blog_list"),
    path("blog-add/",blog_add,name="blog_add"),
    path("blog-edit/<id>/",blog_edit,name="blog_edit"),
    path("blog-remove/<id>/",blog_remove,name="blog_remove"),
    path("blog-comment/",blog_comment,name="blog_comment"),
    path("blog-comment-remove-<id>/",blog_comment_remove,name="blog_comment_remove"),
    path("category-list/",category,name="category"),
    path("category-remove-<id>/",category_remove,name="category_remove"),
    path("user/superuser/",super_user,name="super_user"),  
    path("user/superuser/edit/<id>/",super_user_edit,name="super_user_edit"),  
    path("user/superuser/remove/<id>/",super_user_remove,name="super_user_remove"),  
    path("user/user-list/",user_list,name="user_list"),  
    path("user/user-edit/<id>/",user_edit,name="user_edit"),  
    path("user/user-remove/<id>/",user_remove,name="user_remove"),  
    path("user/user-follower/",user_follower,name="user_follower"),  
    path("product/add-product/",add_product,name="add_product"),  
    path("product/product-list/",product_list,name="product_list"),  
    path("product/product-edit/<id>/",product_edit,name="product_edit"),  
    path("product/product-remove/<id>/",product_remove,name="product_remove"),  
    path("order/order-list/",order_list,name="order_list"),  
    path("order/order-edit-<id>/",order_edit,name="order_edit"),  
]
