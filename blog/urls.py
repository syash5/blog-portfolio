from django.urls import path
from blog.views import  article_create , article_list ,about, home_page, query_create , contact_us


urlpatterns = [
    path('create/', article_create, name="article_create"),
    path('article_list', article_list, name="article_list"),
    # re_path(r'^(?P<slug>[\w-]+)/$', article_list, name="article_list"),
    path('about/', about, name="about"),
    path('contact_us/', contact_us, name="contact_us"),
    path('', home_page, name="home_page"),
    path('query/', query_create, name="query_create")

]
