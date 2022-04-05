from typing import Dict

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from comments.models import Comment
from likes.models import LikeDislike
from posts.models import Post
from users.serializers import UserPublicSerializer


class PostSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()
    author = UserPublicSerializer(source="user", required=False)
    stats = serializers.SerializerMethodField()

    def get_stats(self, obj):
        request = self.context.get("request")
        counts = {
            "likes_count": LikeDislike.objects.filter(
                post_id=obj.id, is_like=True
            ).count(),
            "dislikes_count": LikeDislike.objects.filter(
                post_id=obj.id, is_like=False
            ).count(),
            "comments_count": Comment.objects.filter(post_id=obj.id).count(),
            "has_liked": LikeDislike.objects.filter(
                post_id=obj.id, user=request.user, is_like=True
            ).exists(),
            "has_disliked": LikeDislike.objects.filter(
                post_id=obj.id, user=request.user, is_like=False
            ).exists(),
        }
        return counts

    class Meta:
        model = Post
        fields: list = ["id", "photo", "description", "timestamp", "author", "stats"]

    def create(self, data: Dict[str, str]) -> Post:
        request = self.context.get("request")
        post = Post.objects.create(
            description=data["description"], photo=data["photo"], user=request.user
        )
        post.save()
        return post
