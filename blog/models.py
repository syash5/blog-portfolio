from django.db import models
from users.models import UserProfile



class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(UserProfile ,on_delete= models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + '...'


class Query(models.Model):

    full_name= models.CharField(max_length=50, default="",blank= False)
    contact_no = models.IntegerField(blank=True)
    detail = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name