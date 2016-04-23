from django.shortcuts import render
from rest_framework import viewsets
from users.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
