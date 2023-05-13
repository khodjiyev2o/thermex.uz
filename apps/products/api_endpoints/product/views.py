from rest_framework.generics import ListAPIView
from apps.products.models import Product
from apps.products.api_endpoints.product.serializers import ProductListSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(brand=self.kwargs.get('pk'))
