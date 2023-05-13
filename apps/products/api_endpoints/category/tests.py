from rest_framework.test import APITestCase
from apps.products.models import Category
from apps.common.choices import category_choices, category_choices_translations
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class TestCategoryView(APITestCase):
    url = reverse('category-list')

    def setUp(self):
        self.user = User.objects.create(first_name='Samandar', phone='+998913665113')
        for category in category_choices:
            Category.objects.create(name_uz=category, name_ru=category_choices_translations[category])

    def test_category_list_russian(self):
        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.user.tokens.get('access')}",
            'HTTP_ACCEPT_LANGUAGE': 'ru'
        }
        response = self.client.get(self.url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ['id', 'name']
        assert response.json()[0]['id'] == 1
        assert response.json()[0]['name'] == category_choices_translations[category_choices[0]]
        assert response.json()[1]['name'] == category_choices_translations[category_choices[1]]
        assert response.json()[1]['id'] == 2

    def test_category_list_uzbek(self):
        headers = {
            'HTTP_AUTHORIZATION': f"Bearer {self.user.tokens.get('access')}",
            'HTTP_ACCEPT_LANGUAGE': 'uz'
        }
        response = self.client.get(self.url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ['id', 'name']
        assert response.json()[0]['id'] == 1
        assert response.json()[0]['name'] == category_choices[0]
        assert response.json()[1]['name'] == category_choices[1]
        assert response.json()[1]['id'] == 2

    def test_category_list_no_auth_uzbek(self):
        response = self.client.get(self.url)
        assert response.json()['detail'] == 'Autentifikatsiya maʼlumotlari taqdim etilmagan.'

    def test_category_list_no_auth_russian(self):
        headers = {'HTTP_ACCEPT_LANGUAGE': 'ru'}
        response = self.client.get(self.url, **headers)
        assert response.json()['detail'] == 'Учетные данные для аутентификации не были предоставлены.'
