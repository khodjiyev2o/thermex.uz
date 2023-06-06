from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from apps.catalogue.models import PrizeChildCategory, PrizeParentCategory, PrizeProduct


User = get_user_model()


class TestPrizeProductView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Samandar", phone="+998913665113")
        self.parent_category = PrizeParentCategory.objects.create(name_uz="Maishiy Texnika", name_ru="Бытовая техника")
        self.child_category = PrizeChildCategory.objects.create(
            name_uz="Telefonlar", name_ru="Телефоны", parent_category=self.parent_category
        )
        self.prize_product = PrizeProduct.objects.create(
            name="Iphone 12 Pro", description="256 gb memory", category=self.child_category
        )

    def test_prize_product_list(self):
        url = reverse("prize-product-list", kwargs={"pk": self.prize_product.id})
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "name", "sell_point", "photo", "description"]
        assert response.json()[0]["name"] == self.prize_product.name
        assert response.json()[0]["sell_point"] == self.prize_product.sell_point
        assert response.json()[0]["description"] == self.prize_product.description

    def test_prize_product_list_wrong_pk(self):
        url = reverse("prize-product-list", kwargs={"pk": 1231122})
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_prize_product_list_no_auth_russian(self):
        url = reverse("prize-product-list", kwargs={"pk": 1})
        headers = {"HTTP_ACCEPT_LANGUAGE": "ru"}
        response = self.client.get(url, **headers)
        assert response.json()["detail"] == "Учетные данные для аутентификации не были предоставлены."
