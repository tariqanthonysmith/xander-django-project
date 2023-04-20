from django.shortcuts import render

from rest_framework import generics
from user.serializers import UserSerilizer, TokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    """View to handle creating a user"""

    serializer_class = UserSerilizer

class CreateTokenView(ObtainAuthToken):


    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES