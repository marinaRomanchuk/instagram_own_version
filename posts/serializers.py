from typing import Dict

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Post
        fields: list = ["id", "photo", "description", "timestamp", "user_id"]

    def create(self, data: Dict[str, str]) -> Post:
        request = self.context.get("request")
        post = Post.objects.create(
            description=data["description"], photo=data["photo"], user=request.user
        )
        post.save()
        return post
