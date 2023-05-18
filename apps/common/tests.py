from rest_framework.test import APITestCase

from django.urls import reverse
from apps.common.models import Region, City, Notification
from django.contrib.auth import get_user_model
from apps.common.choices import REGION_CHOICES
User = get_user_model()


class TestProfile(APITestCase):
    regions = REGION_CHOICES

    def setUp(self):

        for region in self.regions.keys():
            new_region = Region.objects.create(name=region)
            for city in self.regions[region]:
                City.objects.create(name=city, region=new_region)

    def test_get_regions_list(self):
        response = self.client.get(reverse("region-list"))
        self.assertEqual(response.status_code, 200)
        assert len(response.json()) == Region.objects.all().count()

    def test_get_regions_serializer(self):
        response = self.client.get(reverse("region-list"))
        self.assertEqual(response.status_code, 200)
        assert list(response.json()[0].keys()) == ['name', 'cities']

    def test_get_regions_names(self):
        response = self.client.get(reverse("region-list"))
        self.assertEqual(response.status_code, 200)
        assert list([region['name'] for region in response.json()]) == list(REGION_CHOICES.keys())

    def test_get_regions_cities_name(self):
        response = self.client.get(reverse("region-list"))
        self.assertEqual(response.status_code, 200)
        for region in response.json():
            city = region['name']
            assert list([city['name'] for city in region['cities']]) == list(REGION_CHOICES[city])


class TestNotificationView(APITestCase):
    url = reverse("notification-list")

    def setUp(self):
        self.user = User.objects.create(phone='+998913665113', first_name='Samandar')
        self.notification = Notification.objects.create(title='Test Title', text='Test Text')

    def test_list_notification_no_auth(self):
        response = self.client.get(self.url)
        assert response.status_code == 401

    def test_list_notification(self):
        headers = {'HTTP_AUTHORIZATION': f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(self.url, **headers)
        assert response.status_code == 200
        assert list(response.json()[0].keys()) == ['id', 'title', 'text', 'image', 'date']
        assert response.json()[0]['id'] == self.notification.id
        assert response.json()[0]['title'] == self.notification.title
