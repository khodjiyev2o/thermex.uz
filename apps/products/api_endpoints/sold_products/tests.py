import tempfile

from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from django.urls import reverse

from django.contrib.auth import get_user_model
from apps.products.models import Category, Brand, Product
from apps.common.choices import category_choices, category_choices_translations, category_brand_dict,\
    brand_product_dict
from apps.products.models import SoldProduct
User = get_user_model()


class SoldProductCreateTestCase(APITestCase):
    image = Image.new("RGB", (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    image.save(tmp_file)
    tmp_file.seek(0)

    def setUp(self) -> None:
        self.url = reverse("sold-product-create")
        self.user = User.objects.create_user(phone="+998123456789", first_name='Samandar')
        self.used_barcode = 1112
        self.new_barcode = 2256
        category_instance = Category.objects.create(name='Test Category')
        brand_instance = Brand.objects.create(name='Test Brand', category=category_instance)
        self.product_instance = Product.objects.create(name='Test Product', brand=brand_instance)
        SoldProduct.objects.create(product=self.product_instance,
                                   user=self.user, barcode=self.used_barcode,)

    def test_create_sold_product_with_valid_data(self):
        headers = {'HTTP_AUTHORIZATION': f"Bearer {self.user.tokens.get('access')}"}

        data = {
            "product": 1,
            "barcode": 1112312,
            "photo": self.tmp_file,
        }
        response = self.client.post(self.url, data=data, format="multipart", **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        image = Image.new("RGB", (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        image.save(tmp_file)
        tmp_file.seek(0)

        data2 = {
            "product": self.product_instance.id,
            "barcode": self.used_barcode,
            "photo": tmp_file,
        }
        response = self.client.post(self.url, data=data2, format="multipart", **headers)
        assert response.json()['non_field_errors'] == ['The fields barcode, product must make a unique set.']

        image = Image.new("RGB", (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        image.save(tmp_file)
        tmp_file.seek(0)

        data3 = {
            "product": self.product_instance.id,
            "barcode": self.new_barcode,
            "photo": tmp_file,
        }
        response = self.client.post(self.url, data=data3, format="multipart", **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)