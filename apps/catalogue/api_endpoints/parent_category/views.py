from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.catalogue.api_endpoints.parent_category.serializers import (
    PrizeParentCategoryListSerializer,
)
from apps.catalogue.models import PrizeParentCategory


class PrizeParentCategoryListView(ListAPIView):
    queryset = PrizeParentCategory.objects.all()
    serializer_class = PrizeParentCategoryListSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["PrizeParentCategoryListView"]
