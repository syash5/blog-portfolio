from django import forms
from . import models
from blog.models import Article
from blog.models import Query
from users.models import UserProfile


class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'thumb',]

class Query(forms.ModelForm):
    class Meta:
        model= Query
        fields = [ 'contact_no','full_name', 'detail']



