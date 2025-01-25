from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import CustomUser
from .factories import CustomUserFactory


@mark.django_db
class UserViewSetTest(APITestCase):
    def setUp(self):
        self.register_url: str = reverse("user-register")
        self.login_url: str = reverse("user-login")

    def test_create_user(self):
        self.assertEqual(CustomUser.objects.count(), 0)
        payload = {
            "first_name": "TestUser",
            "last_name": "TestUserLastName",
            "email": "test-email@example.com",
            "password": "test-password",
        }
        with self.assertNumQueries(5):
            res = self.client.post(self.register_url, data=payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            res_json = res.json()
            self.assertEqual(CustomUser.objects.count(), 1)
            new_user = CustomUser.objects.first()
            self.assertEqual(new_user.first_name, payload["first_name"])
            self.assertEqual(new_user.last_name, payload["last_name"])
            self.assertEqual(new_user.email, payload["email"])
            self.assertNotIn("password", res_json)

    def test_user_login(self):
        payload = {"email": "test-user@example.com", "password": "test-password"}
        user = CustomUser.objects.create_user(**payload)
        with self.assertNumQueries(1):
            res = self.client.post(self.login_url, data=payload)
            self.assertEqual(user.email, payload["email"])
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIn("access_token", res.data)
            self.assertIn("refresh_token", res.data)
