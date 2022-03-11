from typing import Union

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from instagram_own_version.permissions import IsAuthor
from likes.models import LikeDislike
from posts.models import Post
from posts.serializers import PostSerializer
from users.models import Followers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthor,)
    serializer_class = PostSerializer

    def list(self, request) -> Response:
        queryset = Post.objects.all()

        try:
            user_id: Union[int, None] = int(self.request.GET.get("user_id"))
        except (ValueError, TypeError):
            user_id = None
        show_feed: bool = self.request.GET.get("feed") == "true"
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if show_feed:
            following: list = Followers.objects.filter(
                follower=self.request.user
            ).values_list("following", flat=True)
            queryset = queryset.filter(user__in=following)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class LikeDislikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk: int):
        counts = {
            "likes_count": LikeDislike.objects.filter(post_id=pk, is_like=True).count(),
            "dislike_count": LikeDislike.objects.filter(
                post_id=pk, is_like=False
            ).count(),
        }
        return Response(counts, status=status.HTTP_200_OK)

    def post(self, request, pk: int):
        is_like = "dislike" not in request.path
        LikeDislike.objects.update_or_create(
            user=request.user, post_id=pk, defaults={"is_like": is_like}
        )
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, pk: int) -> Response:
        LikeDislike.objects.filter(post_id=pk, user=request.user).delete()
        return Response(status=status.HTTP_200_OK)
