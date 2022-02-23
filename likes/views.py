from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from likes.models import Dislike, Like
from posts.models import Post


class LikeView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        user = request.user
        post = request.POST["post_id"]
        if Like.objects.filter(post=post).filter(user=user):
            like = Like.objects.get(user=user, post=post)
            like.is_deleted = not like.is_deleted
            like.save()
        else:
            Like.objects.create(user=user, post=Post.objects.get(id=post))
        return Response()


class DislikeView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        user = request.user
        post = request.POST["post_id"]
        if Dislike.objects.filter(post=post).filter(user=user):
            dislike = Dislike.objects.get(user=user, post=post)
            dislike.is_deleted = not dislike.is_deleted
            dislike.save()
        else:
            Dislike.objects.create(user=user, post=Post.objects.get(id=post))
        return Response()
