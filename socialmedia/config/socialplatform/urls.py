from django.urls import path
from socialplatform import views
app_name = 'socialplatform'
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('follow',views.follow,name='follow'),
    path('setting/',views.setting,name='setting'),
    path('profile/<username>',views.profile,name='profile'),
    path('like-post/<post_id>',views.like,name='like'),
    path('comment/',views.comment,name='comment'),
    path('upload/',views.upload,name='upload'),
    path('delete/<post_id>',views.delete,name='delete'),
    path('del/<comment_slug>',views.dlcomment,name='dlcomment'),
    path('search',views.search,name='search'),

]