from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.products.api_endpoints.product.serializers import ProductListSerializer
from apps.products.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(brand=self.kwargs.get("pk"))
