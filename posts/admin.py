from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", "description", "timestamp", "user", "is_deleted")
    search_fields = ("timestamp", "description")


admin.site.register(Post, PostAdmin)
