from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from posts.models import Post
from users.models import User


class PostTest(APITestCase):
    def setUp(self):
        self.signup_data = {"username": "harrypotter", "password": "hogwarts934"}
        self.client.post(reverse("signup"), self.signup_data)
        post = Post(
            photo="data:image/gif;base64,R0lGODlhEAAOALMAAOazToeHh0tLS/7LZv/0jvb29t"
            "/f3//Ub//ge8WSLf/rhf/",
            description="picture",
            user=User.objects.get(username=self.signup_data.get("username")),
        )
        post.save()

    def get_argument(self, username):
        return {"pk": User.objects.get(username=username).id}

    def authenticate(self, login_data):
        response = self.client.post(reverse("token"), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.last()
        token = Token.objects.get(user=user)
        self.assertEqual(response.data["token"], token.key)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


class RetrievePostTest(PostTest):
    def test_can_retrieve_self_post(self):
        self.authenticate(self.signup_data)
        response = self.client.get(reverse("post-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePostTest(PostTest):
    def test_can_update_self_post(self):
        self.authenticate(self.signup_data)
        response = self.client.patch(
            reverse("post-detail", kwargs={"pk": 2}), {"description": "new one"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
