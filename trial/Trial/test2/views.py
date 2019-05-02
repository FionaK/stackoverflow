#from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from test2.serializers import UserSerializer, GroupSerializer

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    """
    api endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewset(viewsets.ModelViewSet):
    """
    api endpoint that allows group to be edited or viewed
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
