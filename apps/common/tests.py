# from rest_framework.test import APITestCase
#
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from apps.common.models import Region
# from apps.common.choices import City
#
#
# class TestProfile(APITestCase):
#     def setUp(self):
#         self.region = Region.objects.create(city=City.Namangan, name='Namangan shahar')
#         self.user = get_user_model().objects.create_user(
#             phone="+998972081018",
#             password="12345678",
#             first_name="Samandar",
#             last_name="Hojiev",
#             middle_name="Ulugbek",
#             username="khodjiyev2o",
#             job=Job.Sotuvchi,
#             date_of_birth='2004-04-20',
#             has_team=True,
#             team_size=5,
#             region=self.region,
#             email="samandarkhodjiyev@gmail.com",
#         )
#         self.maxDiff = None
#
#     def test_update_profile(self):
#         data = {
#             "first_name": "Updated first_name",
#             "last_name": "Updated last_name",
#             "username": "updated username",
#         }
#         headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
#         response = self.client.patch(reverse("profile-update"), data=data, **headers)
#         expected_response = {
#             "id": self.user.id,
#             "username": "updated username",
#             "first_name": "Updated first_name",
#             "last_name": "Updated last_name",
#             "middle_name": "Ulugbek",
#             "job": Job.Sotuvchi,
#             "date_of_birth": '2004-04-20',
#             "email": "samandarkhodjiyev@gmail.com",
#             "photo": None,
#             "phone": "+998972081018",
#             'has_team': True,
#             'team_size': 5,
#             'region': {
#                 'city': 'Namangan', 'name': 'Namangan shahar'
#             },
#         }
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), expected_response)
