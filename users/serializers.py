from rest_framework import serializers

from .models import Followers, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "description",
            "date_of_birth",
            "profile_photo",
        ]


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = ["follower", "following", "timestamp"]
