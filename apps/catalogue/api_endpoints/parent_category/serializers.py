from rest_framework import serializers

from apps.catalogue.models import PrizeParentCategory


class PrizeParentCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrizeParentCategory
        fields = ("id", "name", "photo")
