from rest_framework.test import APITestCase

from apps.products.models import Category, Brand, Product
from apps.common.choices import category_choices, category_choices_translations, category_brand_dict,\
    brand_product_dict
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class TestProductView(APITestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Samandar', phone='+998913665113')
        self.brands = []
        for category in category_choices:
            category_instance = Category.objects.create(name_uz=category,
                                                        name_ru=category_choices_translations[category])
            for brand in category_brand_dict[category]:
                self.brands.append(brand)
                brand_instance = Brand.objects.create(name=brand, category=category_instance)
                for product in brand_product_dict[brand]:
                    Product.objects.create(name=product, brand=brand_instance)

    def test_product_list(self):
        url = reverse('product-list', kwargs={'pk': 2})
        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        assert response.status_code == 200
        # assert list(response.json()[0].keys()) == ['id', 'name', 'point']
        # assert len(response.json()) == len(brand_product_dict[self.brands[0]])
        # assert response.json()[0]['name'] == brand_product_dict[self.brands[0]][0]

    def test_product_list_no_auth_russian(self):
        url = reverse('product-list', kwargs={'pk': 1})
        headers = {'HTTP_ACCEPT_LANGUAGE': 'ru'}
        response = self.client.get(url, **headers)
        assert response.json()['detail'] == 'Учетные данные для аутентификации не были предоставлены.'