from rest_framework import serializers

from apps.products.models import UserBoughtProduct


class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBoughtProduct
        fields = ("id", "thermex_product", "prize_product")
