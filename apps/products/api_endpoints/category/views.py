from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.products.api_endpoints.category.serializers import CategoryListSerializer
from apps.products.models import Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAuthenticated]
