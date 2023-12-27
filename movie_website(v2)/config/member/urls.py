from django.urls import path
from . import views
app_name = "member"

urlpatterns = [
        path('',views.step_one,name="step_one"),
        path('step_two',views.step_two,name="step_two"),
        path('profile/update',views.update,name="update"),
]
