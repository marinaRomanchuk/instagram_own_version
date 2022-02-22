from django.conf.urls import url

from comments.views import CommentViewSet

comments = CommentViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

comment_detail = CommentViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    url(r"^comments/$", comments, name="comments"),
    url(r"^comments/(?P<pk>\d+)/$", comment_detail, name="comment-detail"),
]
