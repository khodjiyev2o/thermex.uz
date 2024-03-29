from django.http import JsonResponse
from fcm_django.models import FCMDevice
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.common.choices import REGION_CHOICES
from apps.common.models import Notification, Occupation, Region
from apps.common.serializers import (
    DeviceRegisterSerializer,
    NotificationListSerializer,
    OccupationListSerializer,
    RegionListSerializer,
)


class RegionNamesListView(APIView):
    def get(self, request):
        cities = list(REGION_CHOICES.keys())
        return JsonResponse({"cities": cities})


class RegionListView(ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()


class OccupationListView(ListAPIView):
    serializer_class = OccupationListSerializer
    queryset = Occupation.objects.all()


class NotificationListView(ListAPIView):
    serializer_class = NotificationListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(created_at__gt=self.request.user.created_at)


class DeviceRegisterView(CreateAPIView):
    queryset = FCMDevice.objects.all()
    serializer_class = DeviceRegisterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user.first_name, user=self.request.user)
