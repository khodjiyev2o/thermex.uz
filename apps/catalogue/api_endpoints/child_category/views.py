from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.catalogue.api_endpoints.child_category.serializers import (
    PrizeChildCategoryListSerializer,
)
from apps.catalogue.models import PrizeChildCategory


class PrizeChildCategoryListView(ListAPIView):
    serializer_class = PrizeChildCategoryListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PrizeChildCategory.objects.filter(parent_category=self.kwargs.get("pk"))


__all__ = ["PrizeChildCategoryListView"]
