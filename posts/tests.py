from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from posts.models import Post
from users.models import Followers, User


class PostTest(APITestCase):
    def setUp(self):
        self.signup_data = {"username": "harrypotter", "password": "hogwarts934"}
        self.signup_data_another = {
            "username": "robinsoncrusoe",
            "password": "daniel1719",
        }
        self.client.post(reverse("signup"), self.signup_data)
        self.client.post(reverse("signup"), self.signup_data_another)
        post = Post(
            photo="data:image/gif;base64,R0lGODlhEAAOALMAAOazToeHh0tLS/7LZv/0jvb29t"
            "/f3//Ub//ge8WSLf/rhf/",
            description="picture",
            user=User.objects.get(username=self.signup_data.get("username")),
        )
        post.save()
        self.timestamp = post.timestamp

        follower = Followers(
            follower=User.objects.get(
                username=self.signup_data_another.get("username")
            ),
            following=User.objects.get(username=self.signup_data.get("username")),
        )
        follower.save()

    def authenticate(self, login_data):
        response = self.client.post(reverse("token"), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user = User.objects.get(username=login_data.get("username"))
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.data["token"], token.key)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


class RetrievePostTest(PostTest):
    def test_str(self):
        post = Post.objects.get(timestamp=self.timestamp)
        self.assertEqual(str(post), f"{post.user.username}'s post")


class ListPostTest(PostTest):
    def test_can_retrieve_self_list(self):
        self.authenticate(self.signup_data)
        response = self.client.get(reverse("posts-list"), {"user_id": self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_feed_list(self):
        self.authenticate(self.signup_data_another)
        response = self.client.get(reverse("posts-list"), {"feed": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
