from django.urls import path

from likes.views import DislikeView, LikeView

urlpatterns = [
    path("like/", LikeView.as_view({"post": "post"}), name="set-like"),
    path("dislike/", DislikeView.as_view({"post": "post"}), name="set-dislike"),
]
