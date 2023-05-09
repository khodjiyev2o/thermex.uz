from django.urls import path

from .views import RegionListView, CityListView, RegionDetailView

application_urlpatterns = [
    path("regions/", RegionListView.as_view(), name="region-list"),
    path("regions/<str:city>", RegionDetailView.as_view(), name="region-detail"),
    path('cities/', CityListView.as_view(), name='city-list'),
]

urlpatterns = application_urlpatterns
