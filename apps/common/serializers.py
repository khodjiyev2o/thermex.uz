from fcm_django.models import FCMDevice
from rest_framework import serializers

from apps.common.models import City, Notification, Occupation, Region


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            "id",
            "name",
        )


class RegionListSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, source="regions")

    class Meta:
        model = Region
        fields = ("name", "cities")


class OccupationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = (
            "id",
            "name",
        )


class NotificationListSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source="created_at")

    class Meta:
        model = Notification
        fields = ("id", "title", "text", "image", "date")


class DeviceRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ("device_id", "registration_id", "type")
