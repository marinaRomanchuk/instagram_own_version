from django.conf.urls import url
from django.urls import path

from users.views import RetrieveUpdateUserProfileView, SignupView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    url(r"^users/(?P<pk>\d+)/$", RetrieveUpdateUserProfileView.as_view()),
]
