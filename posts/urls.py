from django.conf.urls import url

from posts.views import PostViewSet

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

urlpatterns: list = [
    url(r"^posts/create/$", post_create, name="create-post"),
    url(r"^posts/$", posts_list, name="posts-list"),
    url(r"^posts/(?P<pk>\d+)/$", posts_detail, name="post-detail"),
]
