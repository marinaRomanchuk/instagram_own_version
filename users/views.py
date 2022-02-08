from rest_framework import generics
from rest_framework.permissions import AllowAny

from instagram_own_version.permissions import IsOwner
from users.models import User
from users.serializers import SignupSerializer, UserPrivateSerializer


class SignupView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = UserPrivateSerializer
    lookup_field = "id"
