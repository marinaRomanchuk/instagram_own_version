from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import SetupSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SetupSerializer
