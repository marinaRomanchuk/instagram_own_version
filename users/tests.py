from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from users.models import User


class UserTest(APITestCase):
    def setUp(self) -> None:
        self.signup_data: Dict[str, str] = {
            "username": "harrypotter",
            "password": "hogwarts934",
        }
        self.client.post(reverse("signup"), self.signup_data)
        self.data: dict = {
            "first_name": "",
            "last_name": "",
            "description": None,
            "username": "harrypotter",
            "date_of_birth": None,
            "profile_photo": None,
            "id": User.objects.get(username="harrypotter").id,
            "email": "",
        }

        self.signup_data_another: Dict[str, str] = {
            "username": "robinsoncrusoe",
            "password": "daniel1719",
        }
        self.client.post(reverse("signup"), self.signup_data_another)
        self.data_another_user: dict = {
            "first_name": "",
            "last_name": "",
            "description": None,
            "username": self.signup_data_another.get("username"),
            "profile_photo": None,
            "id": User.objects.get(username="robinsoncrusoe").id,
        }

    def get_argument(self, username: str) -> dict:
        return {"pk": User.objects.get(username=username).id}

    def authenticate(self, login_data: dict) -> None:
        response = self.client.post(reverse("token"), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(username=login_data.get("username"))
        token = Token.objects.get(user=user)
        self.assertEqual(response.data["token"], token.key)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)


class CreateUserTest(APITestCase):
    def setUp(self) -> None:
        self.signup_data: Dict[str, str] = {
            "username": "harrypotter",
            "password": "hogwarts934",
        }
        self.signup_data_another: Dict[str, str] = {
            "username": "robinsoncrusoe",
            "password": "123",
        }

    def test_can_create_user(self) -> None:
        response = self.client.post(reverse("signup"), self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_not_create_user(self) -> None:
        response = self.client.post(reverse("signup"), self.signup_data_another)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(reverse("signup"), self.signup_data)

        response = self.client.post(reverse("signup"), self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RetrieveUserTest(UserTest):
    def test_str(self) -> None:
        user = User.objects.get(username=self.signup_data.get("username"))
        self.assertEqual(str(user), user.username)

    def test_can_retrieve_self_user(self) -> None:
        self.authenticate(self.signup_data)
        response = self.client.get(
            reverse("user", kwargs=self.get_argument(self.signup_data["username"]))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.data)

    def test_can_retrieve_another_user(self) -> None:
        self.authenticate(self.signup_data)
        response = self.client.get(
            reverse(
                "user",
                kwargs=self.get_argument(self.signup_data_another["username"]),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.data_another_user)


class UpdateUserTest(UserTest):
    def setUp(self) -> None:
        super().setUp()
        self.data: dict = {
            "first_name": "Harry",
            "last_name": "Potter",
            "description": "Boy",
        }

    def test_can_update_self_user(self) -> None:
        self.authenticate(self.signup_data)
        response = self.client.patch(
            reverse("user", kwargs=self.get_argument(self.signup_data["username"])),
            self.data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_update_another_user(self) -> None:
        self.authenticate(self.signup_data)
        response = self.client.patch(
            reverse(
                "user",
                kwargs=self.get_argument(self.signup_data_another["username"]),
            ),
            {"first_name": "Alex"},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
