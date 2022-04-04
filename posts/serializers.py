from typing import Dict

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Post
from users.serializers import UserPublicSerializer


class PostSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()
    user_info = UserPublicSerializer(source="user", required=False)

    class Meta:
        model = Post
        fields: list = ["id", "photo", "description", "timestamp", "user_info"]

    def create(self, data: Dict[str, str]) -> Post:
        request = self.context.get("request")
        post = Post.objects.create(
            description=data["description"], photo=data["photo"], user=request.user
        )
        post.save()
        return post
