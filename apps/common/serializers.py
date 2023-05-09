from apps.common.models import Region
from rest_framework import serializers


class RegionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ("name",)


class RegionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ("name",'city')
