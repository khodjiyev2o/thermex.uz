from apps.common.models import Region
from rest_framework import serializers


class RegionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ("city", "name")
