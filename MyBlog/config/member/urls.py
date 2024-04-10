from django.urls import path
from . import views as member
from django.contrib.auth import views

app_name = "member"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # path("login/", views.login, name="login"),
    path("register/", member.register, name="register"),
    path("logout/", member.logout, name="logout"),
    path("profile/", member.profile, name="profile"),
    path("top_user/", member.top_user, name="top_user"),
    path("user-profile/<id>", member.user_profile, name="user_profile"),
    path("follow/<id>", member.follow, name="follow"),
    path("my-blog/", member.myblog, name="myblog"),
    path("change-password/", member.change, name="change"),
    path("check/code/<username>/<email>/<id>", member.check, name="check"),
]
