from django.contrib.auth.password_validation import validate_password
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from users.models import Followers, User


class UserPublicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    profile_photo = Base64ImageField()
    relations = serializers.SerializerMethodField()

    def get_relations(self, obj):
        request = self.context.get("request")
        if request:
            return {
                "followed": Followers.objects.filter(
                    following=obj.id, follower=request.user
                ).exists()
            }
        return {"followed": False}

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "description",
            "profile_photo",
            "relations",
        ]


class UserPrivateSerializer(UserPublicSerializer):
    username = serializers.CharField(read_only=True)

    class Meta(UserPublicSerializer.Meta):
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "description",
            "date_of_birth",
            "profile_photo",
            "email",
        ]


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields: tuple = ("username", "password", "id")

    def validate(self, attrs: dict) -> dict:
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError(
                {"username": "There is a user with the same username."}
            )
        return attrs

    def create(self, validated_data: dict) -> User:
        user = User.objects.create(
            username=validated_data["username"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
