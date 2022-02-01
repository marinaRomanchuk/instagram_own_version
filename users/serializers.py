from rest_framework import serializers

from users.models import User


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "description",
            "profile_photo",
        ]


class UserPrivateSerializer(UserPublicSerializer):
    class Meta(UserPublicSerializer.Meta):
        fields = [
            "username",
            "first_name",
            "last_name",
            "description",
            "date_of_birth",
            "profile_photo",
        ]
