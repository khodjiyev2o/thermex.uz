from rest_framework import serializers
from apps.products.models import Category


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')
