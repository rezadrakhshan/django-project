from django.urls import path
from . import views

app_name = "list"

urlpatterns = [
    path('',views.list,name="list"),
    path('done/<slug>',views.done,name="done"),
    path('undo/<slug>',views.undo,name="undo"),
    path('delete/<slug>',views.delete,name="delete"),


]
