from rest_framework import filters, generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from instagram_own_version.permissions import IsOwner
from users.models import Followers, User
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


class RetrieveUpdateSelfUserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwner,)
    serializer_class = UserPrivateSerializer

    def get_object(self):
        return self.request.user


class SearchUserView(generics.ListAPIView):
    search_fields = ["username", "first_name", "last_name"]
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer


class FollowerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk: int):
        Followers.objects.update_or_create(follower=request.user, following_id=pk)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, pk: int) -> Response:
        to_delete = Followers.objects.filter(follower=request.user, following_id=pk)
        if to_delete:
            to_delete.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
