from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics

from apps.accounts.serializers import UserSerializer, LogInSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
