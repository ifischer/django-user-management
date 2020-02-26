from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from user_management.serializers import UserSerializer


class UserView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
