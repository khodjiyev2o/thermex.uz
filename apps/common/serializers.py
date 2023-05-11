from apps.common.models import Region, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


class RegionListSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, source='regions')

    class Meta:
        model = Region
        fields = ("name", 'cities')

