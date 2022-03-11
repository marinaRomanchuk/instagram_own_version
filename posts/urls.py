from django.conf.urls import url

from posts.views import LikeDislikeViewSet, PostViewSet

post_create = PostViewSet.as_view(
    {
        "post": "create",
    }
)

posts_list = PostViewSet.as_view(
    {
        "get": "list",
    }
)

posts_detail = PostViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

set_like = LikeDislikeViewSet.as_view(
    {
        "post": "post",
        "delete": "destroy",
    }
)

urlpatterns = [
    url(r"^posts/create/$", post_create, name="create-post"),
    url(r"^posts/$", posts_list, name="posts-list"),
    url(r"^posts/(?P<pk>\d+)/$", posts_detail, name="post-detail"),
    url(r"^posts/(?P<pk>\d+)/like/$", set_like, name="set-like"),
    url(r"^posts/(?P<pk>\d+)/dislike/$", set_like, name="set-dislike"),
    url(
        r"^posts/(?P<pk>\d+)/likes/count/$",
        LikeDislikeViewSet.as_view({"get": "get"}),
        name="likes_count",
    ),
]
