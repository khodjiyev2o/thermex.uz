from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.products.models import SoldProduct
from apps.users.api_endpoints.profile.detail.serializers import UserRegionListSerializer
from apps.users.models import User


class CreateSoldProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProduct
        fields = ("product", "photo", "barcode", "city")

    def validate_barcode(self, value):
        product = self.initial_data.get("product")

        if product and SoldProduct.objects.filter(barcode=value, product=product).exists():
            raise serializers.ValidationError(_("Этот продукт уже добавлен !"))
        if len(value) != 14 or not value.startswith("0"):
            raise serializers.ValidationError(_("Неверный бар код!"))
        return value


class ListSoldProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    point = serializers.CharField(source="product.point")
    city = UserRegionListSerializer()

    class Meta:
        model = SoldProduct
        fields = ("id", "product", "photo", "barcode", "point", "created_at", "city")


class UserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("points",)
