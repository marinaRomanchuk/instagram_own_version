from django.conf.urls import url
from django.urls import path

from users.views import (
    RetrieveUpdateUserProfileView,
    RetrieveUserProfileView,
    SearchUserView,
    SignupView,
)

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    url(r"^users/(?P<pk>\d+)/$", RetrieveUserProfileView.as_view(), name="user"),
    url("users/me/", RetrieveUpdateUserProfileView.as_view(), name="me"),
    url("search/", SearchUserView.as_view(), name="search_user"),
]
