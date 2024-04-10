"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("", include("member.urls")),  
    path("", include("blog.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("shop/", include("shop.urls")),
    path("", include("django.contrib.auth.urls")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

handler404 = 'main.views.custom_page_not_found'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
