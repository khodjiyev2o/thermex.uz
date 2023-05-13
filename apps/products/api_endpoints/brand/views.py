from rest_framework.generics import ListAPIView
from apps.products.models import Brand
from apps.products.api_endpoints.brand.serializers import BrandListSerializer
from rest_framework.permissions import IsAuthenticated


class BrandListView(ListAPIView):
    serializer_class = BrandListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Brand.objects.filter(category=self.kwargs.get('pk'))
