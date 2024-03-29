from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class CheckUsernameTestCase(APITestCase):
    def test_check_avialable_username(self):
        url = reverse("check-username")
        data = {"username": "test_username"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), {"success": True, "message": "Username is available"})

    def test_check_existing_username(self):
        User.objects.create_user(username="test_username", password="test_password", phone="+998935961151")
        url = reverse("check-username")
        data = {"username": "test_username"}
        headers = {"HTTP_ACCEPT_LANGUAGE": "ru"}
        response = self.client.post(url, data, **headers)
        self.assertDictEqual(response.json(), {"username": "Имя пользователя уже используется"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
