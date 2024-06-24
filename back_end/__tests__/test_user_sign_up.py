from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from rest_framework.authtoken.models import Token

from user_app.serializers import AppUserSerializer, AppUser
from user_app.interfaces import UserData, UserRegistrationData
import json


class UserSignUp(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data: UserData = {
            "first_name": "Francisco",
            "last_name": "Avila",
            "email": "fr@fr.com",
            "password": "p3r553u5",
        }

    def test_user_sign_up_success(self):
        response = self.client.post(
            reverse("login_signup"),
            data=self.user_data,
            content_type="application/json",
        )
        with self.subTest():
            self.assertEqual(response.status_code, 201)
        body: UserRegistrationData = json.loads(response.content)
        self.assertTrue(
            body.get("user") == AppUserSerializer(AppUser.objects.first()).data
            and body.get("token") == Token.objects.get(user=AppUser.objects.first()).key
        )

    def test_login_user_success(self):
        signup = self.client.post(
            reverse("login_signup"),
            data=self.user_data,
            content_type="application/json",
        )
        with self.subTest():
            self.assertEqual(signup.status_code, 201)
        del self.user_data["first_name"]
        del self.user_data["last_name"]
        response = self.client.post(
            reverse("login_signup"),
            data=self.user_data,
            content_type="application/json",
        )
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        body: UserRegistrationData = json.loads(response.content)
        self.assertTrue(
            body.get("user") == AppUserSerializer(AppUser.objects.first()).data
            and body.get("token") == Token.objects.get(user=AppUser.objects.first()).key
        )
