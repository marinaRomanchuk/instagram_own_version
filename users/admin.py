from django.contrib import admin

from .models import Followers, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "description",
        "profile_photo",
    )
    search_fields = ("username", "first_name", "last_name")


class FollowersAdmin(admin.ModelAdmin):
    list_display = ("follower", "following", "timestamp")
    search_fields = ("timestamp", "follower", "following")


admin.site.register(User, UserAdmin)
admin.site.register(Followers, FollowersAdmin)
