from rest_framework import serializers

from comments.models import Comment
from users.serializers import UserPublicSerializer


class CommentSerializer(serializers.ModelSerializer):
    users = UserPublicSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields: list = ["text", "post_id", "users", "timestamp"]
