from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "post", "timestamp", "user")
    search_fields = ("timestamp", "post")


admin.site.register(Comment, CommentAdmin)
