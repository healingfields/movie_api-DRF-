from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from djJson.models import User


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "example",
            "email": "example@xyz.com",
            "password": "postgres123",
            "password2": "postgres123"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="testUser", password="postgres123")

    def test_login(self):
        data = {
            "username": "testUser",
            "password": "postgres123"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="testUser")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
