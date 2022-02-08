from django.conf.urls import url
from django.urls import path

from users.views import SignupView, UpdateProfileView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    url(r"^(?P<id>\d+)/$", UpdateProfileView.as_view()),
]
