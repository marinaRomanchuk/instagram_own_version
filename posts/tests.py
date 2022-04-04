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
        self.signup_data["id"] = User.objects.get(
            username=self.signup_data.get("username")
        ).id
        self.client.post(reverse("signup"), self.signup_data_another)
        self.signup_data_another["id"] = User.objects.get(
            username=self.signup_data_another.get("username")
        ).id

        self.data = {
            "photo": "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH"
            "ElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
            "description": "red dot",
        }

    def authenticate(self, login_data):
        response = self.client.post(reverse("token"), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user = User.objects.get(id=login_data.get("id"))
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.data["token"], token.key)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


class CreatePostTest(PostTest):
    def test_can_create_post(self):
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("create-post"), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ListPostTest(PostTest):
    def setUp(self):
        super().setUp()
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("create-post"), self.data)
        self.data["timestamp"] = response.json()["timestamp"]
        self.post_id = Post.objects.get(timestamp=self.data["timestamp"]).id

        follower = Followers(
            follower=User.objects.get(id=self.signup_data_another.get("id")),
            following=User.objects.get(id=self.signup_data.get("id")),
        )
        follower.save()

    def test_str(self):
        post = Post.objects.get(timestamp=self.data.get("timestamp"))
        self.assertEqual(str(post), f"{post.user.username}'s post")

    def test_can_retrieve_self_list(self):
        self.authenticate(self.signup_data)
        response = self.client.get(reverse("posts-list"), {"user_id": self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_feed_list(self):
        self.authenticate(self.signup_data_another)
        response = self.client.get(reverse("posts-list"), {"feed": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_post(self):
        self.authenticate(self.signup_data_another)
        response = self.client.delete(
            reverse("post-detail", kwargs={"pk": self.post_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_delete_post(self):
        self.authenticate(self.signup_data_another)
        response = self.client.delete(reverse("post-detail", kwargs={"pk": 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class LikeDislikeTest(PostTest):
    def setUp(self):
        super().setUp()
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("create-post"), self.data)
        self.data["timestamp"] = response.json()["timestamp"]
        self.data["id"] = Post.objects.get(timestamp=self.data["timestamp"]).id

    def test_set_like_dislike(self):
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("set-like", kwargs={"pk": self.data["id"]}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            reverse("set-dislike", kwargs={"pk": self.data["id"]})
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_number_of_likes_dislikes(self):
        self.authenticate(self.signup_data)
        self.client.post(reverse("set-like", kwargs={"pk": self.data["id"]}))
        self.authenticate(self.signup_data_another)
        self.client.post(reverse("set-like", kwargs={"pk": self.data["id"]}))

        response = self.client.get(reverse("stats", kwargs={"pk": self.data["id"]}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {
                "comments_count": 0,
                "dislikes_count": 0,
                "likes_count": 2,
                "has_liked": True,
                "has_disliked": False,
            },
            response.json(),
        )

        response = self.client.get(reverse("stats", kwargs={"pk": self.data["id"]}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {
                "comments_count": 0,
                "dislikes_count": 0,
                "likes_count": 2,
                "has_liked": True,
                "has_disliked": False,
            },
            response.json(),
        )

    def test_delete_like_dislike(self):
        self.authenticate(self.signup_data)
        self.client.post(reverse("set-like", kwargs={"pk": self.data["id"]}))

        response = self.client.delete(
            reverse("set-like", kwargs={"pk": self.data["id"]})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
