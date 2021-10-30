from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import slugify

# Create your models here.
class Admin(models.Model):
    advisor_name = models.CharField(max_length=20)
    advisor_profile_pic = models.ImageField(upload_to ='G/')
    advisor_id = models.IntegerField(default=True)
    booking_time = models.DateTimeField(auto_now_add=True,null=True)
    booking_id = models.AutoField(primary_key=True)

class Signup(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=50)
    user_id = models.AutoField(primary_key=True)

class Date(models.Model):
    geeks = models.DateTimeField(auto_now_add=True,null=True,blank=True)

class Login(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id
