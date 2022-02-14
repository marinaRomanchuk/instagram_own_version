from rest_framework import viewsets
from rest_framework.response import Response

from instagram_own_version.permissions import IsAuthor
from posts.models import Post
from posts.serializers import PostSerializer
from users.models import Followers, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthor,)
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()
        user_parameter = int(self.request.GET.get("user_id", None))
        feed_parameter = self.request.GET.get("feed", None)
        if user_parameter:
            user_obj = User.objects.get(id=user_parameter)
            if feed_parameter:
                fol = Followers.objects.filter(follower=user_obj).values_list(
                    "following", flat=True
                )
                queryset = queryset.filter(user__in=fol)
            else:
                queryset = queryset.filter(user=user_obj)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
