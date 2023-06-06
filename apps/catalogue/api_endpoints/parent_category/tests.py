from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.catalogue.models import PrizeParentCategory


User = get_user_model()


class TestCategoryView(APITestCase):
    url = reverse("prize-category-list")

    def setUp(self):
        self.user = User.objects.create(first_name="Samandar", phone="+998913665113")
        PrizeParentCategory.objects.create(name_uz="Maishiy Texnika", name_ru="Бытовая техника")

    def test_category_list_russian(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}", "HTTP_ACCEPT_LANGUAGE": "ru"}
        response = self.client.get(self.url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "name"]
        assert response.json()[0]["name"] == "Бытовая техника"

    def test_category_list_uzbek(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}", "HTTP_ACCEPT_LANGUAGE": "uz"}
        response = self.client.get(self.url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "name"]
        assert response.json()[0]["name"] == "Maishiy Texnika"

    def test_category_list_no_auth_russian(self):
        headers = {"HTTP_ACCEPT_LANGUAGE": "ru"}
        response = self.client.get(self.url, **headers)
        assert response.json()["detail"] == "Учетные данные для аутентификации не были предоставлены."
