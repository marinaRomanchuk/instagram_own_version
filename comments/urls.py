from django.conf.urls import url

from comments.views import CommentViewSet

comment_add = CommentViewSet.as_view(
    {
        "post": "create",
    }
)

comments_list = CommentViewSet.as_view(
    {
        "get": "list",
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
    url(r"^comments/add/$", comment_add, name="add-comment"),
    url(r"^comments/$", comments_list, name="comments-list"),
    url(r"^comments/(?P<pk>\d+)/$", comment_detail, name="comment-detail"),
]
