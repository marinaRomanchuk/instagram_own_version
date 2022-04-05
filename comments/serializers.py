from typing import Dict

from rest_framework import serializers

from comments.models import Comment
from users.serializers import UserPublicSerializer


class CommentSerializer(serializers.ModelSerializer):
    user_info = UserPublicSerializer(source="user", required=False)

    class Meta:
        model = Comment
        fields = ["text", "post", "timestamp", "user_info"]

    def create(self, data: Dict) -> Comment:
        request = self.context.get("request")
        comment = Comment.objects.create(
            text=data["text"], post=data["post"], user=request.user
        )
        return comment
