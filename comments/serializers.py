from typing import Dict

from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "post", "timestamp"]

    def create(self, data: Dict) -> Comment:
        request = self.context.get("request")
        comment = Comment.objects.create(
            text=data["text"], post=data["post"], user=request.user
        )
        return comment
