from rest_framework import generics

from instagram_own_version.permissions import IsAuthor
from posts.models import Post
from posts.serializers import PostSerializer


class RetrieveUpdateDestroyPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthor,)
    serializer_class = PostSerializer
