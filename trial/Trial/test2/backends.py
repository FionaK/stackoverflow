from django.contrib.auth.models import user
from django.contrib.auth.hashers import check_password
from django.conf import settings



class MyBackend:
    def authenticate(self, request, username=none, password=none)
    """
    check the username and password and return a valid user
    """
