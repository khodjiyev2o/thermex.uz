from rest_framework import serializers

from apps.catalogue.models import PrizeChildCategory


class PrizeChildCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrizeChildCategory
        fields = ("id", "name")
