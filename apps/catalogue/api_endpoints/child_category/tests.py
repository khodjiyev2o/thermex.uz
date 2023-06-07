from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.catalogue.models import PrizeChildCategory, PrizeParentCategory


User = get_user_model()


class TestChildCategoryView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Samandar", phone="+998913665113")
        self.parent_category = PrizeParentCategory.objects.create(name_uz="Maishiy Texnika", name_ru="Бытовая техника")
        self.child_category = PrizeChildCategory.objects.create(
            name_uz="Telefonlar", name_ru="Телефоны", parent_category=self.parent_category
        )

    def test_child_category_list_russian(self):
        url = reverse("prize-child-category-list", kwargs={"pk": self.parent_category.id})
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "name", "photo"]
        assert response.json()[0]["name"] == self.child_category.name_ru
        assert response.json()[0]["id"] == self.child_category.id

    def test_child_category_list_uzbek(self):
        url = reverse("prize-child-category-list", kwargs={"pk": self.parent_category.id})
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}", "HTTP_ACCEPT_LANGUAGE": "uz"}
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "name", "photo"]
        assert response.json()[0]["name"] == self.child_category.name_uz
        assert response.json()[0]["id"] == self.child_category.id

    def test_child_category_list_wrong_pk(self):
        url = reverse("prize-child-category-list", kwargs={"pk": 111111})
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_brand_list_no_auth_russian(self):
        url = reverse("prize-child-category-list", kwargs={"pk": self.parent_category.id})
        headers = {"HTTP_ACCEPT_LANGUAGE": "ru"}
        response = self.client.get(url, **headers)
        assert response.json()["detail"] == "Учетные данные для аутентификации не были предоставлены."
