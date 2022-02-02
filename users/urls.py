from django.urls import path

from users.views import GetUser, RegisterUser

urlpatterns = [
    path("register/", RegisterUser.as_view()),
    path("get_users/", GetUser.as_view()),
]
