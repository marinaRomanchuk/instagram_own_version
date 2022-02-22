from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from comments.models import Comment
from posts.models import Post
from users.models import User


class CommentTest(APITestCase):
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

        self.post_data = {
            "photo": "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH"
            "ElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
            "description": "red dot",
        }
        self.authenticate(self.signup_data_another)
        response = self.client.post(reverse("create-post"), self.post_data)
        self.post_data["timestamp"] = response.json()["timestamp"]
        self.post_data["id"] = Post.objects.get(
            timestamp=self.post_data["timestamp"]
        ).id
        self.comment_data = {
            "text": "Beautiful",
            "post": self.post_data["id"],
        }

    def authenticate(self, login_data):
        response = self.client.post(reverse("token"), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user = User.objects.get(id=login_data.get("id"))
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.data["token"], token.key)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


class CreateCommentTest(CommentTest):
    def test_can_add_comment(self):
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("add-comment"), self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ListCommentTest(CommentTest):
    def setUp(self):
        super().setUp()
        self.authenticate(self.signup_data)
        response = self.client.post(reverse("add-comment"), self.comment_data)
        self.comment_data["timestamp"] = response.json()["timestamp"]
        self.comment_id = Comment.objects.get(
            timestamp=self.comment_data["timestamp"]
        ).id

    def test_str(self):
        comment = Comment.objects.get(timestamp=self.comment_data.get("timestamp"))
        self.assertEqual(str(comment), comment.text)

    def test_can_retrieve_list_of_comments(self):
        self.authenticate(self.signup_data_another)
        response = self.client.get(
            reverse("comments-list"), {"post_id": self.post_data["id"]}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [self.comment_data])

    def test_can_retrieve_list_of_all_comments(self):
        self.authenticate(self.signup_data_another)
        response = self.client.get(reverse("comments-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_comment(self):
        self.authenticate(self.signup_data_another)
        response = self.client.get(
            reverse("comment-detail", kwargs={"pk": self.comment_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.comment_data)
