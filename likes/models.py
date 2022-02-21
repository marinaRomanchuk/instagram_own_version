from django.db import models


class Like(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name: str = "Like"
        verbose_name_plural: str = "Likes"


class Dislike(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name: str = "Dislike"
        verbose_name_plural: str = "Dislikes"
