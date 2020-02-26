from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView
from user_management.serializers import UserSerializer


class ListUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
