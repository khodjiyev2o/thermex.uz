from rest_framework import serializers

from apps.products.models import SoldProduct
from apps.users.api_endpoints.profile.detail.serializers import UserRegionListSerializer


class CreateSoldProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProduct
        fields = ("product", "photo", "barcode", "city")


class ListSoldProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    point = serializers.CharField(source="product.point")
    city = UserRegionListSerializer()

    class Meta:
        model = SoldProduct
        fields = ("id", "product", "photo", "barcode", "point", "created_at", "city")
