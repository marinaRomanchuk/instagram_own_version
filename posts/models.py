from django.db import models


class Post(models.Model):
    photo = models.ImageField()
    description = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.timestamp
