from django.shortcuts import render
from django.contrib.auth import aauthenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import routers, viewsets
from .serializers import UserSerializer


# Create your views here.

def index(request):
    return HttpResponse("Hello")


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer