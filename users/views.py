from rest_framework import generics
from rest_framework.permissions import AllowAny

from instagram_own_version.permissions import IsOwner
from users.models import User
from users.serializers import (
    SignupSerializer,
    UserPrivateSerializer,
    UserPublicSerializer,
)


class SignupView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


class RetrieveUpdateUserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwner,)

    def get_serializer_class(self):
        # todo cache object to not query the database twice
        if self.request.user == self.get_object():
            return UserPrivateSerializer
        return UserPublicSerializer
