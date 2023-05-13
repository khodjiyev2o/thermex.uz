from rest_framework import serializers
from apps.products.models import SoldProduct


class CreateSoldProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoldProduct
        fields = ('product', 'photo', 'barcode')
