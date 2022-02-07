from django.conf.urls import url
from django.urls import path

from users.views import GetView, SignupView, UpdateView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    url(r"^(?P<username>\w+)/edit/$", UpdateView.as_view(), name="update"),
    url(r"^(?P<username>\w+)/get/$", GetView.as_view(), name="get"),
]
