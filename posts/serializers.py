from rest_framework import serializers

from posts.models import Post
from users.serializers import UserPublicSerializer


class PostSerializer(serializers.ModelSerializer):
    users = UserPublicSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["photo", "description", "timestamp", "user"]
