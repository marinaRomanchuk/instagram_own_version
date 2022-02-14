from django.conf.urls import url

from posts.views import PostViewSet

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

urlpatterns = [
    url(r"^posts/$", posts_list, name="posts-list"),
    url(r"^posts/(?P<pk>\d+)/$", posts_detail, name="post-detail"),
]
