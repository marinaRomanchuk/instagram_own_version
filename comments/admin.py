from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "post", "timestamp", "user", "is_deleted")
    search_fields = ("timestamp", "post")


admin.site.register(Comment, CommentAdmin)
