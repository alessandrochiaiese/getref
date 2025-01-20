import logging
from django.http import JsonResponse 
from django.contrib.auth.models import User 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from accounts.api.serializers import UserSerializer

# Set up a logger
logger = logging.getLogger(__name__) 

class UserList(generics.ListCreateAPIView):
    permission_classes = [AllowAny] #, permissions,IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [AllowAny] #, permissions,IsAuthenticated,  TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

