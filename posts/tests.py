from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from posts.models import Post
from users.models import Followers, User


class PostTest(APITestCase):
    def setUp(self) -> None:
        self.signup_data: dict = {"username": "harrypotter", "password": "hogwarts934"}
        self.signup_data_another: dict = {
            "username": "robinsoncrusoe",
            "password": "daniel1719",
        }
        self.client.post(reverse("signup"), self.signup_data)
        self.signup_data["id"] = User.objects.get(
            username=self.signup_data.get("username")
        ).id
        self.client.post(reverse("signup"), self.signup_data_another)
        self.signup_data_another["id"] = User.objects.get(
            username=self.signup_data_another.get("username")
        ).id

        self.data: dict = {
            "photo": "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH"
            "ElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
            "description": "red dot",
        }

    def authenticate(self, login_data: dict) -> None:
        response = self.client.post(reverse("token"), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user = User.objects.get(id=login_data.get("id"))
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.data["token"], token.key)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


class CreatePostTest(PostTest):
    def test_can_create_post(self) -> None:
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("create-post"), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ListPostTest(PostTest):
    def setUp(self) -> None:
        super().setUp()
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("create-post"), self.data)
        self.data["timestamp"] = response.json()["timestamp"]

        follower = Followers(
            follower=User.objects.get(id=self.signup_data_another.get("id")),
            following=User.objects.get(id=self.signup_data.get("id")),
        )
        follower.save()

    def test_str(self) -> None:
        post = Post.objects.get(timestamp=self.data.get("timestamp"))
        self.assertEqual(str(post), f"{post.user.username}'s post")

    def test_can_retrieve_self_list(self) -> None:
        self.authenticate(self.signup_data)
        response = self.client.get(reverse("posts-list"), {"user_id": self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_feed_list(self) -> None:
        self.authenticate(self.signup_data_another)
        response = self.client.get(reverse("posts-list"), {"feed": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
