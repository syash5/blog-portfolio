"""funky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import os
from django.conf import settings
from django.contrib import admin
from django.urls import re_path
from django.urls import path, include
from users.views import (user_login, user_logout,register_view, success)
from blog.views import (article_create, article_detail, article_list,about, query_create, contact_us, home_page)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_view/', register_view, name="register_view"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('create/', article_create, name="article_create"),
    path('article_list', article_list, name="article_list"),
    # re_path(r'^(?P<slug>[\w-]+)/$', article_list, name="article_list"),
    path('about/', about,name="about"),
    path('contact_us/', contact_us,name="contact_us"),
    path('success/', success, name="user_success"),
    path('', home_page, name="home_page"),
    path('query/', query_create, name="query_create" )
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)