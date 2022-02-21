from django.contrib import admin

from .models import Followers, User


class UserAdmin(admin.ModelAdmin):
    list_display: tuple = (
        "username",
        "first_name",
        "last_name",
        "description",
        "profile_photo",
    )
    search_fields: tuple = ("username", "first_name", "last_name")


class FollowersAdmin(admin.ModelAdmin):
    list_display: tuple = ("follower", "following", "timestamp")
    search_fields: tuple = ("timestamp", "follower", "following")


admin.site.register(User, UserAdmin)
admin.site.register(Followers, FollowersAdmin)
