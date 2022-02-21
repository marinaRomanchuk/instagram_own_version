from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display: tuple = ("text", "post", "timestamp", "user")
    search_fields: tuple = ("timestamp", "post")


admin.site.register(Comment, CommentAdmin)
