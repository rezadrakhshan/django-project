from django.urls import path
from .views import *

app_name = "shop"
urlpatterns = [path("detail-<id>/", detail, name="detail")]
