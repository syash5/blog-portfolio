from django.urls import path
from users.views import register_view, user_login, user_logout , success



urlpatterns = [
    path('register_view/', register_view, name="register_view"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('success/', success, name="user_success"),


]