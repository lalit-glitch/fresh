from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Admin,Signup,Date,Login
from django.contrib.auth.models import User

class AdminSerializer(serializers.ModelSerializer):
   class Meta:
       model = Admin
       fields = ['advisor_name','advisor_profile_pic']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['user_id','name','email','password']

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['geeks']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['advisor_id','advisor_name','advisor_profile_pic','booking_time','booking_id']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['advisor_id','advisor_name','advisor_profile_pic']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['user_id','email','password']






