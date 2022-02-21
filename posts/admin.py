from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display: tuple = ("id", "photo", "description", "timestamp", "user")
    search_fields: tuple = ("timestamp", "description")


admin.site.register(Post, PostAdmin)
