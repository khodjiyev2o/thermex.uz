from django.urls import path

from .views import RegionListView, RegionNamesListView

application_urlpatterns = [
    path("regions/", RegionListView.as_view(), name="region-list"),
    # path("regions/<str:city>", RegionDetailView.as_view(), name="region-detail"),
    path('cities/', RegionNamesListView.as_view(), name='region-names-list'),
]

urlpatterns = application_urlpatterns
