from django.db import models


class LikeDislike(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_like = models.BooleanField(default=True)

    class Meta:
        verbose_name = "LikeDislike"
        verbose_name_plural = "LikesDislikes"
