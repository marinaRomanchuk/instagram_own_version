from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30, unique=True)
    personal_information = models.TextField(max_length=300)
    profile_photo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.nickname}'


class Post(models.Model):
    photo = models.ImageField()
    description = models.TextField(max_length=500, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.description}'


class Comment(models.Model):
    comment_text = models.TextField(max_length=500)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.comment_text}'


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Dislike(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Dislike'
        verbose_name_plural = 'Dislikes'


class Followers(models.Model):
    follower = models.ForeignKey('User', on_delete=models.CASCADE)
    following = models.ForeignKey('User', on_delete=models.CASCADE)
