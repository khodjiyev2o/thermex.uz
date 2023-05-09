from rest_framework.test import APITestCase

from django.urls import reverse
from apps.common.models import Region
from apps.common.choices import REGION_CHOICES, City


class TestProfile(APITestCase):
    regions = REGION_CHOICES

    def setUp(self):
        for city in self.regions.keys():
            for region in self.regions[city]:
                Region.objects.create(city=city, name=region)

    def test_get_regions_list(self):
        response = self.client.get(reverse("region-list"))
        self.assertEqual(response.status_code, 200)
        assert len(response.json()) == Region.objects.all().count()

    def test_get_regions_detail_list(self):
        response = self.client.get(reverse("region-detail", kwargs={'city': 'Namangan'}))
        self.assertEqual(response.status_code, 200)
        assert sorted([resp['name'] for resp in response.json()]) == sorted(REGION_CHOICES['Namangan'])

    def test_get_cities_list(self):
        response = self.client.get(reverse("city-list"))
        self.assertEqual(response.status_code, 200)
        assert list([city[0] for city in response.json()['cities']]) == list(REGION_CHOICES.keys())
