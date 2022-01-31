from rest_framework import serializers

from .models import Dislike, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["post", "user", "timestamp"]


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ["post", "user", "timestamp"]
