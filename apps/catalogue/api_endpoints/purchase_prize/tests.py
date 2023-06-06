from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.common.models import City, Region
from apps.products.models import Brand, Category, Product, SoldProduct
from apps.catalogue.models import PrizeChildCategory, PrizeParentCategory, PrizeProduct

User = get_user_model()


class TestUserPurchasePrizeProducts(APITestCase):
    url = reverse("prize-product-purchase")

    def setUp(self) -> None:
        self.user = User.objects.create_user(phone="+998123456789", first_name="Samandar")
        self.category_instance = Category.objects.create(name="Test Category")
        self.brand_instance = Brand.objects.create(name="Test Brand", category=self.category_instance)
        self.region_instance = Region.objects.create(name="Namanagan")
        self.city_instance = City.objects.create(region=self.region_instance, name="Davlatobod tumani")
        self.product_instance = Product.objects.create(name="Test Product", brand=self.brand_instance, point=200)
        SoldProduct.objects.create(product=self.product_instance, user=self.user, barcode=1234, city=self.city_instance)

        self.parent_category = PrizeParentCategory.objects.create(name_uz="Maishiy Texnika", name_ru="Бытовая техника")
        self.child_category = PrizeChildCategory.objects.create(
            name_uz="Telefonlar", name_ru="Телефоны", parent_category=self.parent_category
        )
        self.prize_product = PrizeProduct.objects.create(
            name="Iphone 12 Pro", description="256 gb memory", category=self.child_category
        )
        self.expensive_prize_product = PrizeProduct.objects.create(
            name="Iphone 14 Pro", description="256 gb memory", category=self.child_category, sell_point=250
        )
        self.expensive_thermex_product = Product.objects.create(
            name="Test Product 2", brand=self.brand_instance, sell_point=201
        )

    def test_purchase_prize_product_with_valid_data(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        data = {
            "prize_product": self.prize_product.id,
        }
        response = self.client.post(self.url, data=data, **headers)
        print(response.json())
        assert response.status_code == 201
        assert list(response.json().keys()) == ["id", "thermex_product", "prize_product"]

    def test_purchase_thermex_product_with_valid_data(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        data = {
            "thermex_product": self.product_instance.id,
        }
        response = self.client.post(self.url, data=data, **headers)
        print(response.json())
        assert response.status_code == 201
        assert list(response.json().keys()) == ["id", "thermex_product", "prize_product"]

    def test_purchase_thermex_product__without_enough_points(self):
        assert self.user.points == self.product_instance.point
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        data = {
            "thermex_product": self.expensive_thermex_product.id,
        }
        response = self.client.post(self.url, data=data, **headers)
        print("Themex", response.json())
        assert response.status_code == 400
        assert response.json()["detail"] == "Недостаточно баллов!"
        assert self.user.points == self.product_instance.point

    def test_purchase_prize_product_without_enough_points(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        data = {
            "prize_product": self.expensive_prize_product.id,
        }
        response = self.client.post(self.url, data=data, **headers)
        print(response.json())
        assert response.status_code == 400
        assert response.json()["detail"] == "Недостаточно баллов!"
