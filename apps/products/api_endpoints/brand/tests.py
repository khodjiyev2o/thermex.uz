from rest_framework.test import APITestCase
from apps.products.models import Category, Brand
from apps.common.choices import category_choices, category_choices_translations, category_brand_dict
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class TestCategoryView(APITestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='Samandar', phone='+998913665113')
        for category in category_choices:
            category_instance = Category.objects.create(name_uz=category,
                                                        name_ru=category_choices_translations[category])
            for brand in category_brand_dict[category]:
                Brand.objects.create(name=brand, category=category_instance)

    def test_brand_list(self):
        url = reverse('brand-list', kwargs={'pk': 1})
        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(url, **headers)
        category_name = category_choices[0]
        assert response.status_code == 200
        assert len(response.json()) == len(category_brand_dict[category_name])
        assert list(response.json()[0].keys()) == ['id', 'name']

    def test_category_list_no_auth_uzbek(self):
        url = reverse('brand-list', kwargs={'pk': 1})
        response = self.client.get(url)
        assert response.json()['detail'] == 'Autentifikatsiya maʼlumotlari taqdim etilmagan.'

    def test_category_list_no_auth_russian(self):
        url = reverse('brand-list', kwargs={'pk': 1})
        headers = {'HTTP_ACCEPT_LANGUAGE': 'ru'}
        response = self.client.get(url, **headers)
        assert response.json()['detail'] == 'Учетные данные для аутентификации не были предоставлены.'
