from django.urls import path

from .views import RegionListView, RegionNamesListView, OccupationListView, NotificationListView, DeviceRegisterView

application_urlpatterns = [
    path("regions/", RegionListView.as_view(), name="region-list"),
    path('cities/', RegionNamesListView.as_view(), name='region-names-list'),
    path('occupations/', OccupationListView.as_view(), name='occupation-list'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('device/register/', DeviceRegisterView.as_view(), name='device-register'),
]

urlpatterns = application_urlpatterns
