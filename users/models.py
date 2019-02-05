from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserProfile(AbstractUser):

    username = models.CharField('username', max_length=150, unique=True, default="")
    full_name= models.CharField(max_length=50, default="",blank= False)
    password= models.CharField(max_length=50,blank=False, default="")
    email = models.EmailField(unique=True, blank=False)
    contact_no = models.IntegerField(unique=True ,null=True)
    Address = models.CharField(max_length=512)


    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = ['username']  # required when user is created

    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = "users"

