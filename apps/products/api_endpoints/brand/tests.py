from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase


from apps.products.models import Brand, Category


User = get_user_model()


class TestBrandView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Samandar", phone="+998913665113")
        self.category = Category.objects.create(name_uz="category", name_ru="category_ru")
        self.brand = Brand.objects.create(name="brand", category=self.category)

    def test_brand_list(self):
        url = reverse("brand-list", kwargs={"pk": self.category.id})
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "name"]

    def test_brand_list_wrong_pk(self):
        url = reverse("brand-list", kwargs={"pk": 11111111111})
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_brand_list_no_auth_russian(self):
        url = reverse("brand-list", kwargs={"pk": 1})
        headers = {"HTTP_ACCEPT_LANGUAGE": "ru"}
        response = self.client.get(url, **headers)
        assert response.json()["detail"] == "Учетные данные для аутентификации не были предоставлены."
