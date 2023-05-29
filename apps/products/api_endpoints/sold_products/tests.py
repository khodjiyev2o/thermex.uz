import tempfile

from PIL import Image
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.models import City, Region
from apps.products.models import Brand, Category, Product, SoldProduct


User = get_user_model()


class TestUserSoldProducts(APITestCase):
    image = Image.new("RGB", (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    image.save(tmp_file)
    tmp_file.seek(0)

    def setUp(self) -> None:
        self.url = reverse("sold-product-create")
        self.user = User.objects.create_user(phone="+998123456789", first_name="Samandar")
        self.used_barcode = 1112
        self.new_barcode = 2256
        region_instance = Region.objects.create(name="Namanagan")
        self.city_instance = City.objects.create(region=region_instance, name="Davlatobod tumani")
        category_instance = Category.objects.create(name="Test Category")
        brand_instance = Brand.objects.create(name="Test Brand", category=category_instance)
        self.product_instance = Product.objects.create(name="Test Product", brand=brand_instance)
        SoldProduct.objects.create(
            product=self.product_instance, user=self.user, barcode=self.used_barcode, city=self.city_instance
        )

    def test_create_sold_product_with_valid_data(self):
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}

        data = {
            "product": self.product_instance.id,
            "barcode": 1112312,
            "photo": self.tmp_file,
            "city": 1,
        }
        response = self.client.post(self.url, data=data, format="multipart", **headers)
        print(response.json())
        print(response.status_code)

        image = Image.new("RGB", (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        image.save(tmp_file)
        tmp_file.seek(0)

        data2 = {
            "product": self.product_instance.id,
            "barcode": self.used_barcode,
            "photo": tmp_file,
            "city": self.city_instance.id,
        }
        response = self.client.post(self.url, data=data2, format="multipart", **headers)
        assert list(response.json().keys()) == ["non_field_errors"]
        image = Image.new("RGB", (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        image.save(tmp_file)
        tmp_file.seek(0)

        data3 = {
            "product": self.product_instance.id,
            "barcode": self.new_barcode,
            "photo": tmp_file,
            "city": 1,
        }
        response = self.client.post(self.url, data=data3, format="multipart", **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_points(self):
        url = reverse("sold-product-user-points")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(url, **headers)
        assert response.json()["success"] is True
        assert response.json()["message"] == "Successfull"
        assert response.json()["points"] == self.product_instance.point

    def test_user_points_no_token(self):
        url = reverse("sold-product-user-points")
        response = self.client.get(url)
        assert response.status_code == 401
        assert response.json()["detail"] == "Учетные данные для аутентификации не были предоставлены."


class TestUserSoldProductsPoint(APITestCase):
    image = Image.new("RGB", (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    image.save(tmp_file)
    tmp_file.seek(0)

    def setUp(self) -> None:
        self.url = reverse("sold-product-create")
        self.user = User.objects.create_user(phone="+998123456789", first_name="Samandar")
        region_instance = Region.objects.create(name="Namanagan")
        city_instance = City.objects.create(region=region_instance, name="Davlatobod tumani")
        category_instance = Category.objects.create(name="Test Category")
        brand_instance = Brand.objects.create(name="Test Brand", category=category_instance)
        self.product_instance = Product.objects.create(name="Test Product", brand=brand_instance)
        self.sold_product = SoldProduct.objects.create(
            product=self.product_instance, user=self.user, barcode="1234", city=city_instance
        )

    def test_user_sold_products_list(self):
        url = reverse("sold-product-user-list")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ["id", "product", "photo", "barcode", "point", "created_at", "city"]
        assert response.json()[0]["product"] == self.product_instance.name
        assert response.json()[0]["barcode"] == self.sold_product.barcode
        assert response.json()[0]["point"] == f"{self.product_instance.point}"

    def test_user_sold_products_no_token(self):
        url = reverse("sold-product-user-list")
        response = self.client.get(url)
        assert response.status_code == 401
        assert response.json()["detail"] == "Учетные данные для аутентификации не были предоставлены."
