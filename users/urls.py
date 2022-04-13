from django.conf.urls import url
from django.urls import path

from users.views import (
    FollowerViewSet,
    RetrieveUpdateSelfUserProfileView,
    RetrieveUserProfileView,
    SearchUserView,
    SignupView,
)

set_follower = FollowerViewSet.as_view(
    {
        "post": "post",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    url(r"^users/(?P<pk>\d+)/$", RetrieveUserProfileView.as_view(), name="user"),
    url("users/me/", RetrieveUpdateSelfUserProfileView.as_view(), name="me"),
    url("search/", SearchUserView.as_view(), name="search_user"),
    url(r"^users/(?P<pk>\d+)/follow/$", set_follower, name="set-follower"),
]
