from rest_framework import viewsets
from rest_framework.response import Response

from instagram_own_version.permissions import IsAuthor
from posts.models import Post
from posts.serializers import PostSerializer
from users.models import Followers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthor,)
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()

        try:
            user_id = int(self.request.GET.get("user_id"))
        except (ValueError, TypeError):
            user_id = None
        show_feed = self.request.GET.get("feed") == "true"
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if show_feed:
            following = Followers.objects.filter(
                follower=self.request.user
            ).values_list("following", flat=True)
            queryset = queryset.filter(user__in=following)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
