from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("photo", "description", "timestamp", "user")
    search_fields = ("timestamp", "description")


admin.site.register(Post, PostAdmin)
