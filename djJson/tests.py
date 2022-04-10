
from rest_framework.test import APITestCase
from .models import StreamPlatform
from django.urls import reverse
from djJson.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token


class StreamPlatformTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="omar", password="postgres123")
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = StreamPlatform.objects.create(name="hbo", about="movies platform", website="https://hbo.com")

    def test_streamplatform_create(self):
        data = {
            "name": "egybest",
            "about": "movie ans series platform",
            "website": "https://www.egybest.com"
        }
        response = self.client.post(reverse('platforms-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatforms_list(self):
        response = self.client.get(reverse('platforms-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_details(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

