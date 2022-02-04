from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer
