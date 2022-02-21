from django.contrib import admin

from .models import Dislike, Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "timestamp", "user")
    search_fields = ("timestamp", "post")


class DislikeAdmin(admin.ModelAdmin):
    list_display = ("post", "timestamp", "user")
    search_fields = ("timestamp", "post")


admin.site.register(Like, LikeAdmin)
admin.site.register(Dislike, DislikeAdmin)
