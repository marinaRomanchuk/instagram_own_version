from rest_framework import filters, generics
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


class RetrieveUserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwner,)

    def get_serializer_class(self):
        # todo cache object to not query the database twice
        if self.request.user == self.get_object():
            return UserPrivateSerializer
        return UserPublicSerializer


class RetrieveUpdateUserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwner,)
    serializer_class = UserPrivateSerializer

    def get_object(self):
        return self.request.user


class SearchUserView(generics.ListAPIView):
    search_fields = ["username", "first_name", "last_name"]
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
