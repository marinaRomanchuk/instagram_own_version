from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Post
from users.serializers import UserPublicSerializer


class PostSerializer(serializers.ModelSerializer):
    users = UserPublicSerializer(many=True, read_only=True)
    photo = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Post
        fields = ["photo", "description", "timestamp", "user"]
