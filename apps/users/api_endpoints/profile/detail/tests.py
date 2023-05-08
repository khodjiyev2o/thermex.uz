from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.common.models import Region
from apps.common.choices import City, Job


class TestProfile(APITestCase):
    def setUp(self):
        self.region = Region.objects.create(city=City.Namangan, name='Namangan shahar')
        self.user = get_user_model().objects.create_user(
            phone="+998972081018",
            password="12345678",
            first_name="Samandar",
            last_name="Hojiev",
            middle_name="Ulugbek",
            username="khodjiyev2o",
            job=Job.Chilangar,
            date_of_birth='2004-04-20',
            has_team=True,
            team_size=5,
            region=self.region,
            email="samandarkhodjiyev@gmail.com",
        )
        self.maxDiff = None

    def test_get_profile(self):
        self.client.login(username=self.user.phone, password="12345678")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(reverse("profile-detail"), **headers)
        self.assertListEqual(list(response.data.keys()),
        ['id', 'username',
         'first_name', 'last_name',
         'middle_name', 'email',
         'photo', 'phone', 'job',
         'date_of_birth', 'has_team',
         'team_size', 'region'])
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['first_name'], self.user.first_name)
        self.assertEqual(response.data['last_name'], self.user.last_name)
        self.assertEqual(response.data['middle_name'], self.user.middle_name)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertEqual(response.data['photo'], self.user.photo)
        self.assertEqual(response.data['has_team'], self.user.has_team)
        self.assertEqual(response.data['team_size'], self.user.team_size)
        self.assertEqual(response.data['date_of_birth'], self.user.date_of_birth)
        self.assertEqual(response.data['job'], self.user.job)
        self.assertEqual(response.json()['region']['name'], self.user.region.name)
        self.assertEqual(response.json()['region']['city'], self.user.region.city)

    def test_get_profile_no_authentication(self):
        self.client.login(username=self.user.phone, password="12345678")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.get(reverse("profile-detail"))
        self.assertEqual(response.json()['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, 401)
