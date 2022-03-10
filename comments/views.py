from typing import Union

from rest_framework import status, viewsets
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentSerializer
from instagram_own_version.permissions import IsAuthor


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_deleted=False)
    permission_classes = (IsAuthor,)
    serializer_class = CommentSerializer

    def list(self, request) -> Response:
        queryset = Comment.objects.filter(is_deleted=False)

        try:
            post_id: Union[int, None] = int(self.request.GET.get("post_id"))
        except (ValueError, TypeError):
            post_id = None

        if post_id:
            queryset = queryset.filter(post_id=post_id)

        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk: int) -> Response:
        comment = Comment.objects.get(id=pk)
        comment.is_deleted = True
        comment.save()
        return Response(status=status.HTTP_200_OK)
