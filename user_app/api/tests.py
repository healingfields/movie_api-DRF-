from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "example10",
            "email": "example10xyz.com",
            "password": "postgres123",
            "password2": "postgres123"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

