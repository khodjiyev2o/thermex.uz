from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.products.api_endpoints.brand.serializers import BrandListSerializer
from apps.products.models import Brand


class BrandListView(ListAPIView):
    serializer_class = BrandListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Brand.objects.filter(category=self.kwargs.get("pk"))
