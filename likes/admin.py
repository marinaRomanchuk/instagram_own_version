from django.contrib import admin

from .models import LikeDislike


class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ("post", "timestamp", "user", "is_like")
    search_fields = ("timestamp", "post")


admin.site.register(LikeDislike, LikeDislikeAdmin)
