from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.catalogue.api_endpoints.prize_product.serializers import ProductListSerializer
from apps.catalogue.models import PrizeProduct


class PrizeProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PrizeProduct.objects.filter(category=self.kwargs.get("pk"))


__all__ = ["PrizeProductListView"]
