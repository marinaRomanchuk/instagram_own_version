from django.db import models


class Post(models.Model):
    photo = models.ImageField(upload_to="post")
    description = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name: str = "Post"
        verbose_name_plural: str = "Posts"

    def __str__(self):
        return f"{self.user.username}'s post"
