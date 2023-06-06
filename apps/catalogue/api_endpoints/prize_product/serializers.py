from rest_framework import serializers

from apps.catalogue.models import PrizeProduct


class PrizeProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrizeProduct
        fields = ("id", "name", "sell_point", "photo", "description")
