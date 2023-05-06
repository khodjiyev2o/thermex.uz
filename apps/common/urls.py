from django.urls import path

from .views import RegionListView, CityListView

application_urlpatterns = [
    path("regions/<str:city>", RegionListView.as_view(), name="region-list"),
    path('cities/', CityListView.as_view(), name='city-list'),
]

urlpatterns = application_urlpatterns
