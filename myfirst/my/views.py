from rest_framework import viewsets
from django.views.generic import ListView
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from my.serializers import UserSerializer,ItemSerializer,AdminSerializer,DateSerializer,ListSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from my.models import Admin,Signup,Date,Login
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class SignupViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = UserSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class ItemListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['advisor_id']

class AdvListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = ListSerializer

class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer


