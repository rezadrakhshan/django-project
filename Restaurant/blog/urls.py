from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('listnews', views.postlist),
    path('order', views.order),
    path('about/', views.about),
    path('order/breakfast/', views.breakfast),
    path('order/lunch', views.lunch),
    path('order/dinner', views.dinner),
    path('order/about/', views.about),
    path('order/listnews', views.postlist),
    path('collection', views.collectionbozorg),
    path('about/collection', views.collectionbozorg),
    path('order/breakfast/collection', views.collectionbozorg),
    path('order/collection', views.collectionbozorg),
    path('order/breakfast/about/', views.collectionbozorg),
    path('booktabel', views.booktabel),    
    path('about/booktabel', views.booktabel),
    path('order/breakfast/booktabel', views.booktabel),
    path('order/booktabel', views.booktabel),
    path('order/about/', views.about),
    path('order/about/collection', views.collectionbozorg),
    path('order/about/booktabel', views.booktabel),
    path('order/about/order', views.order),
       
    

]
