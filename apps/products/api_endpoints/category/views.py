from rest_framework.generics import ListAPIView
from apps.products.models import Category
from apps.products.api_endpoints.category.serializers import CategoryListSerializer
from rest_framework.permissions import IsAuthenticated


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAuthenticated]
