from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

from django_filters.rest_framework import DjangoFilterBackend
class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
