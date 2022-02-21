from django.contrib import admin

from .models import Dislike, Like


class LikeAdmin(admin.ModelAdmin):
    list_display: tuple = ("post", "timestamp", "user")
    search_fields: tuple = ("timestamp", "post")


class DislikeAdmin(admin.ModelAdmin):
    list_display: tuple = ("post", "timestamp", "user")
    search_fields: tuple = ("timestamp", "post")


admin.site.register(Like, LikeAdmin)
admin.site.register(Dislike, DislikeAdmin)
