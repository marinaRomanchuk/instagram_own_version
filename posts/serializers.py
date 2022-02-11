from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Post
        fields = ["photo", "description", "timestamp"]
