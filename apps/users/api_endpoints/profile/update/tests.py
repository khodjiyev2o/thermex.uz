from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.common.choices import REGION_CHOICES, Job
from apps.common.models import City, Occupation, Region


class TestProfile(APITestCase):
    def setUp(self):
        self.region = Region.objects.create(name=list(REGION_CHOICES.keys())[0])
        self.city = City.objects.create(region=self.region, name=REGION_CHOICES.get("Tashkent shahri")[0])
        self.job = Occupation.objects.create(name=Job.Sotuvchi)
        self.user = get_user_model().objects.create_user(
            phone="+998972081018",
            password="12345678",
            first_name="Samandar",
            last_name="Hojiev",
            middle_name="Ulugbek",
            username="khodjiyev2o",
            job=self.job,
            date_of_birth="2004-04-20",
            has_team=True,
            team_size=5,
            city=self.city,
            email="samandarkhodjiyev@gmail.com",
        )
        self.maxDiff = None

    def test_update_profile(self):
        data = {
            "first_name": "Updated first_name",
            "last_name": "Updated last_name",
            "username": "updated username",
        }
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.patch(reverse("profile-update"), data=data, **headers)
        expected_response = {
            "id": self.user.id,
            "username": "updated username",
            "first_name": "Updated first_name",
            "last_name": "Updated last_name",
            "middle_name": "Ulugbek",
            "job": self.job.id,
            "date_of_birth": "2004-04-20",
            "email": "samandarkhodjiyev@gmail.com",
            "photo": None,
            "phone": "+998972081018",
            "has_team": True,
            "team_size": 5,
            "city": self.city.id,
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_update_profile_no_authentication(self):
        data = {
            "first_name": "Updated first_name",
            "last_name": "Updated last_name",
            "username": "updated username",
        }
        response = self.client.patch(reverse("profile-update"), data=data)
        self.assertEqual(response.status_code, 401)
