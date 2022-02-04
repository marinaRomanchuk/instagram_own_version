from django.contrib.auth.password_validation import validate_password
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


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, attrs):
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError(
                {"username": "There is a user with the same username."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
