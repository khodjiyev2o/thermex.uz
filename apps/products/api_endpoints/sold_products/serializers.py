from rest_framework import serializers

from apps.products.models import SoldProduct
from apps.users.api_endpoints.profile.detail.serializers import UserRegionListSerializer
from django.utils.translation import gettext_lazy as _


class CreateSoldProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProduct
        fields = ("product", "photo", "barcode", "city")

    def validate_barcode(self, value):
        product = self.initial_data.get("product")

        if product and SoldProduct.objects.filter(barcode=value, product=product).exists():
            raise serializers.ValidationError(_("Этот продукт уже добавлен !"))

        return value


class ListSoldProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    point = serializers.CharField(source="product.point")
    city = UserRegionListSerializer()

    class Meta:
        model = SoldProduct
        fields = ("id", "product", "photo", "barcode", "point", "created_at", "city")
